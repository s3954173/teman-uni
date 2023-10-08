from django.shortcuts import render, redirect
from .forms import EventForm, InvitedFriendsForm, SubmitEventForm, User, EventUsersGoingForm, EventUsersDeclinedForm
from temanuni.models import Events, EventInvitedUsers, EventUsersDeclined, EventUsersGoing
from django.http import JsonResponse

def events(request):
    if 'user_id' in request.session and request.session['user_id']:
        creator_id = request.session['user_id']  # Retrieve user_id from session

        # Find Event Objects based upon whether user is invited, declined or going to events

        # Invited Events
        invited_users = EventInvitedUsers.objects.using('temanuni').filter(user_id=creator_id)
        invited_events = invited_users.using('temanuni').values_list('event_id', flat=True)
        events_invited = Events.objects.using('temanuni').filter(event_id__in=invited_events)

        #Declined Event
        declined_users = EventUsersDeclined.objects.using('temanuni').filter(user_id=creator_id)
        declined_events = declined_users.using('temanuni').values_list('event_id', flat=True)
        events_declined = Events.objects.using('temanuni').filter(event_id__in=declined_events)

        #Going Events
        going_users = EventUsersGoing.objects.using('temanuni').filter(user_id=creator_id)
        going_events = going_users.using('temanuni').values_list('event_id', flat=True)
        events_going = Events.objects.using('temanuni').filter(event_id__in=going_events)
        
        # Events Created
        events_created = Events.objects.using('temanuni').filter(creator_id=creator_id)


        if request.method == 'POST':
            form = EventForm(request.POST, creator_id=creator_id)
            if form.is_valid():
                creator = User.objects.using('temanuni').get(pk=creator_id)
                # Create an instance of SubmitEventForm and populate its fields
                dbEventForm = SubmitEventForm({
                    'event_name': form.cleaned_data['eventName'],
                    'start_date': form.cleaned_data['eventDate'],
                    'start_time': form.cleaned_data['eventTime'],
                    'description': form.cleaned_data['eventDesc'],
                    'creator_id': creator,
                })
                
                if dbEventForm.is_valid():
                    event = dbEventForm.save(commit=True)
                    for friend in form.cleaned_data['friends']:
                        dbInvitedFriendsForm = InvitedFriendsForm({
                            'event_id': event,
                            'user_id': friend,
                        })
                        if dbInvitedFriendsForm.is_valid():
                            dbInvitedFriendsForm.save(commit=True)
                    return redirect('events')
                else:
                    print("invalid dbEventForm")
                    print(dbEventForm.errors)
        else:
            form = EventForm(creator_id=creator_id)  # Pass user_id as a keyword argument
        return render(request, 'events/eventCreation.html', 
        {'form': form, 'events_invited': events_invited, 'events_declined': events_declined, 'events_going': events_going, 'events_created': events_created }
        )
    else:
        return redirect('home')

def create_event_user(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        event = request.POST.get('event_id')
        user = request.session['user_id']
        if status in ('going', 'declined'):
            if status == 'going':
                form = EventUsersGoingForm({
                    'event_id': event,
                    'user_id': user
                })
            else:
                form = EventUsersDeclinedForm({
                    'event_id': event,
                    'user_id': user
                })

            if form.is_valid():
                dbEventGoingDeclined = form.save(commit=False)
                dbEventGoingDeclined.save(using='temanuni')

                 # Retrieve the corresponding invited_users object
                invited_users = EventInvitedUsers.objects.using('temanuni').filter(event_id=event, user_id=user).first()

                if invited_users:
                    # Delete the invited_users object
                    invited_users.delete(using='temanuni')
                return redirect('events')
            else:
                return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False})




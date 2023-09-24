from django.shortcuts import render, redirect
from .forms import EventForm, InvitedFriendsForm, SubmitEventForm, User

def events(request):
    if 'user_id' in request.session and request.session['user_id']:
        creator_id = request.session['user_id']  # Retrieve user_id from session
        
        if request.method == 'POST':
            form = EventForm(request.POST, creator_id=creator_id)
            print(form.errors)
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
                            print("works!")
                    return redirect('home')
                else:
                    print("invalid dbEventForm")
                    print(dbEventForm.errors)
        else:
            form = EventForm(creator_id=creator_id)  # Pass user_id as a keyword argument
        return render(request, 'events/eventCreation.html', {'form': form})
    else:
        return redirect('home')




    
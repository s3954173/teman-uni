from django.shortcuts import render, redirect
from .forms import EventForm, InvitedFriendsForm, SubmitEventForm

def events(request):
    if 'user_id' in request.session and request.session['user_id']:
        creator_id = request.session['user_id']  # Retrieve user_id from session
        if request.method == 'POST':
            form = EventForm(request.POST, creator_id=creator_id)
            if form.is_valid():
                # Create an instance of SubmitEventForm and populate its fields
                dbEventForm = SubmitEventForm({
                    'eventName': form.cleaned_data['eventName'],
                    'eventDate': form.cleaned_data['eventDate'],
                    'eventTime': form.cleaned_data['eventTime'],
                    'eventDesc': form.cleaned_data['eventDesc'],
                    'creator_id': creator_id,
                })
                
                if dbEventForm.is_valid():
                    dbEventForm = dbEventForm.save(commit=True)
                    event_id = dbEventForm.event_id
                    print(event_id)
                    return redirect('home')
                else:
                    print("invalid dbEventForm")
        else:
            form = EventForm(creator_id=creator_id)  # Pass user_id as a keyword argument
        return render(request, 'events/eventCreation.html', {'form': form})
    else:
        return redirect('home')




    
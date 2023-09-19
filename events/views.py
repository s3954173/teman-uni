from django.shortcuts import render, redirect
from .forms import EventForm, InvitedFriendsForm, SubmitEventForm

def createEvent(request):
    if 'user_id' in request.session and request.session['user_id']:
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                # Create a new event instance with the user as the admin
                event = form.save(commit=False)
                event.eventAdmin = request.user  # Assuming 'eventAdmin' is a ForeignKey to the User model
                event.save()
                return redirect('success_url')  # Replace with the actual URL name or path
        else:
            form = EventForm()

        return render(request, 'events/eventCreation.html', {'form': form})
    else:
        return redirect('home')



    
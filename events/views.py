from django.shortcuts import render, redirect
from .forms import EventForm

# Create your views here.

def createEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.eventAdmin = request.user
            event.save()
            return redirect('success_url')
    else:
        form = EventForm()
    
    

    return render(request, 'events/eventCreation.html', {'form' : form})
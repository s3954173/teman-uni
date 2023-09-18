from django import forms
from temanuni.models import Events
from datetime import datetime
from .models import InvitedFriends


class EventForm(forms.ModelForm):
    eventName = forms.CharField(label='Event Name', required=True)
    eventDate = forms.DateField(label='Event Date', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    eventTime = forms.TimeField(label='Event Time', required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    eventDesc = forms.CharField(label='Event Description', required=True, widget=forms.Textarea)
    creator_id = forms.CharField(label='Event Name', required=True)
    # friends = forms.ModelMultipleChoiceField(
    #     queryset=Friend.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    # )

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        
        # Get the current date and time
        current_datetime = datetime.now()
        
        # Set min attributes for eventDate and eventTime widgets
        self.fields['eventDate'].widget.attrs['min'] = current_datetime.date()
        self.fields['eventTime'].widget.attrs['min'] = current_datetime.strftime('%H:%M')

    class Meta:
        model = Events
        fields = ['eventName', 'eventDate', 'eventTime', 'eventDesc']
   
    
    def clean_eventDesc(self):
        eventDesc = self.cleaned_data.get('eventDesc')
        word_limit = 100
        words = eventDesc.split()
        if len(words) > word_limit:
            raise forms.ValidationError(
                f'Event description cannot exceed {word_limit} words.'
            ) 
        return eventDesc

    def clean_datetime(self):
        cleaned_data = super().clean()
        event_date = cleaned_data.get('eventDate')
        event_time = cleaned_data.get('eventTime')

        if event_date and event_time:
            # Combine event_date and event_time to create a datetime object
            event_datetime = datetime.combine(event_date, event_time)

            # Get the current datetime
            current_datetime = datetime.now()

            # Check if the event_datetime is in the past
            if event_datetime <= current_datetime:
                self.add_error('eventDate', 'Event date and time must be in the future.')


class SubmitEventForm (forms.ModelForm):
    class Meta:
        model = Events
        fields = ['eventName', 'eventDate', 'eventTime', 'eventDesc', 'eventID', 'creatorID']

class InvitedFriendsForm(forms.ModelForm):
    class Meta:
        model = InvitedFriends
        fields = ['friendID', 'eventID']
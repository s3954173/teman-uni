from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
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
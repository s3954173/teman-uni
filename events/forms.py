from django import forms
from temanuni.models import Events


class EventForm(forms.ModelForm):
    eventName = forms.CharField(label='Event Name', required=True)
    eventDate = forms.DateField(label='Event Date', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    eventTime = forms.TimeField(label='Event Time', required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    eventDesc = forms.CharField(label='Event Description', required=True, widget=forms.Textarea)
    # friends = forms.ModelMultipleChoiceField(
    #     queryset=Friend.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    # )

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


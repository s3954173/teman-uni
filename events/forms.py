from django import forms
from temanuni.models import Events, EventInvitedUsers, Friends
from datetime import datetime




class EventForm(forms.ModelForm):
    

    eventName = forms.CharField(label='Event Name', required=True)
    eventDate = forms.DateField(label='Event Date', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    eventTime = forms.TimeField(label='Event Time', required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    eventDesc = forms.CharField(label='Event Description', required=True, widget=forms.Textarea)
    friends = forms.ModelMultipleChoiceField(
        queryset= None,
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        
        user_id = kwargs.pop('user_id', None)  # Retrieve user_id from kwargs
        super(EventForm, self).__init__(*args, **kwargs)

        if user_id is not None:
            # Query friends and populate the 'friends' field based on user_id
            matches = Friends.objects.filter(
                (Q(user1_id=user_id) | Q(user2_id=user_id)) & Q(match_user1=True, match_user2=True)
            )

            friend_user_ids = []

            for match in matches:
                if match.user1_id == user_id:
                    friend_user_ids.append(match.user2_id)
                else:
                    friend_user_ids.append(match.user1_id)

            self.fields['friends'].queryset = friend_user_ids
        
        # Get the current date and time
        current_datetime = datetime.now()
        
        # Set min attributes for eventDate and eventTime widgets
        self.fields['eventDate'].widget.attrs['min'] = current_datetime.date()
        self.fields['eventTime'].widget.attrs['min'] = current_datetime.strftime('%H:%M')

        
   
    
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
    eventName = forms.CharField(label='Event Name', required=True)
    eventDate = forms.DateField(label='Event Date', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    eventTime = forms.TimeField(label='Event Time', required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    eventDesc = forms.CharField(label='Event Description', required=True, widget=forms.Textarea)
    creator_id = forms.IntegerField()
    class Meta:
        model = Events
        fields = ['event_name', 'start_date', 'start_time', 'description', 'creator_id']

class InvitedFriendsForm(forms.ModelForm):
    friendID = forms.CharField(max_length=100)
    eventID = forms.CharField(max_length=100)   
    class Meta:
        model = EventInvitedUsers
        fields = ['friendID', 'eventID']
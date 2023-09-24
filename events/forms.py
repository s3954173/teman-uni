from django import forms
from temanuni.models import Events, EventInvitedUsers, Friends, User
from datetime import datetime
from django.db.models import Q



class EventForm(forms.Form):
    eventName = forms.CharField(label='Event Name', required=True)
    eventDate = forms.DateField(label='Event Date', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    eventTime = forms.TimeField(label='Event Time', required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    eventDesc = forms.CharField(label='Event Description', required=True, widget=forms.Textarea)
    friends = forms.ModelMultipleChoiceField(
        required=True,
        queryset= None,
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        
        creator_id = kwargs.pop('creator_id', None)  # Retrieve creator_id from kwargs
        super(EventForm, self).__init__(*args, **kwargs)
        if creator_id is not None:
            # Query friends and populate the 'friends' field based on creator_id
            matches = Friends.objects.using('temanuni').filter(
                (Q(user1_id=creator_id) | Q(user2_id=creator_id)) & Q(user1_interest=1, user2_interest=1)
            )

            friends = []
            
            for match in matches:
                if match.user1_id.user_id == creator_id:
                    friends.append(match.user2_id.user_id)
                else:
                    friends.append(match.user1_id.user_id)
            
            friends = User.objects.using('temanuni').filter(user_id__in=friends).values_list('user_id', flat=True)
            self.fields['friends'].queryset = User.objects.using('temanuni').filter(user_id__in=friends)

            # friends_id = User.objects.using('temanuni').filter(user_id__in=friends).values_list('user_id', flat=True)
            # self.fields['friends'].queryset = friends_id


            # friends_id = User.objects.using('temanuni').filter(user_id__in=friends)
            # self.fields['friends'].queryset = User.objects.using('temanuni').filter(user_id__in=friend_user_ids)

        
        # Get the current date and time
        current_datetime = datetime.now()
        
        # Set min attributes for eventDate and eventTime widgets
        self.fields['eventDate'].widget.attrs['min'] = current_datetime.date()
        self.fields['eventTime'].widget.attrs['min'] = current_datetime.strftime('%H:%M')

        
   
    
    # def clean_eventDesc(self):
    #     eventDesc = self.cleaned_data.get('eventDesc')
    #     word_limit = 100
    #     words = eventDesc.split()
    #     if len(words) > word_limit:
    #         raise forms.ValidationError(
    #             f'Event description cannot exceed {word_limit} words.'
    #         ) 
    #     return eventDesc

    # def clean_datetime(self):
    #     cleaned_data = super().clean()
    #     event_date = cleaned_data.get('eventDate')
    #     event_time = cleaned_data.get('eventTime')

    #     if event_date and event_time:
    #         # Combine event_date and event_time to create a datetime object
    #         event_datetime = datetime.combine(event_date, event_time)

    #         # Get the current datetime
    #         current_datetime = datetime.now()

    #         # Check if the event_datetime is in the past
    #         if event_datetime <= current_datetime:
    #             self.add_error('eventDate', 'Event date and time must be in the future.')
    
    # class Meta:
    #         fields = ['eventName', 'eventDate', 'eventTime', 'eventDesc', 'friends']



class SubmitEventForm (forms.ModelForm):
    event_name = forms.CharField(label='Event Name', required=True)
    start_date = forms.DateField(label='Event Date', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(label='Event Time', required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    description = forms.CharField(label='Event Description', required=True, widget=forms.Textarea)
    creator_id = forms.ModelChoiceField(queryset=User.objects.using('temanuni').all(), required=True)

    class Meta:
        model = Events
        fields = ['event_name', 'start_date', 'start_time', 'description', 'creator_id']

    def save(self, commit=True, using='temanuni'):
        event = super(SubmitEventForm, self).save(commit=False)
        
        # Set the event_name, start_date, start_time, description, and creator_id fields
        event.event_name = self.cleaned_data['event_name']
        event.start_date = self.cleaned_data['start_date']
        event.start_time = self.cleaned_data['start_time']
        event.description = self.cleaned_data['description']
        event.creator_id = self.cleaned_data['creator_id']
        
        if commit:
            event.save(using=using)  # Save the event to the database

        return event

class InvitedFriendsForm(forms.ModelForm):
    friendID = forms.CharField(max_length=100)
    eventID = forms.CharField(max_length=100)   
    class Meta:
        model = EventInvitedUsers
        fields = ['friendID', 'eventID']
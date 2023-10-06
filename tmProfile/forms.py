from django import forms
from django.forms import ModelForm
from temanuni.models import Profile
from django.forms.fields import DateField
from datetime import datetime


class CustomDateField(DateField):
    def to_python(self, value):
        if value:
            try:
                # Parse the date string into a datetime.date object
                return datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                raise forms.ValidationError('Enter a valid date in YYYY-MM-DD format.')
        return None

class CreateProfile(forms.ModelForm):
    interests = forms.CharField(max_length=255, required=False)  # Non-model field
    languages = forms.CharField(max_length=255, required=False)  # Non-model field
    dob = CustomDateField(input_formats=['%Y-%m-%d'])  # Custom date field

    class Meta:
        model = Profile
        exclude = ['profile_id']  # Exclude profile_id field

    # def save(self, commit=True, using='temanuni'):
    #     profile = super(CreateProfile, self).save(commit=False)
        

        
    #     if commit:
    #         profile.save(using=using)  # Save the event to the database

    #     return profile

    # def __init__(self, *args, **kwargs):
    #     profile_id = kwargs.pop('profile_id', None)  # Retrieve profile_id from kwargs
    #     super(CreateProfile, self).__init__(*args, **kwargs)
    #     if profile_id is not None:
    #         self.fields['profile_id'].initial = profile_id

# class InterestForm(forms.ModelForm):
#     class Meta:
#         model = Interests
#         fields = ['interest']

# class LanguageForm(forms.ModelForm):
#     class Meta:
#         model = Languages
#         fields = ['languages']

        
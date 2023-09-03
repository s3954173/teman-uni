from django import forms
from temanuni.models import User as tmUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class TemanUniUserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email', required=True, help_text="Please enter a valid email") 

    class Meta:
        model = tmUser  # Use your custom user model
        fields = ['email', 'password']
    
    def save(self, commit=True, using='temanuni'):
        user = super(TemanUniUserRegistrationForm, self).save(commit=False)

        # Only set the email and password fields
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password']  # Set the password field

        if commit:
            user.save(using=using)  # Specify the using parameter to save to a different database

        return user

        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True, help_text="Please enter a valid email")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


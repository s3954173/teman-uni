from django import forms
from temanuni.models import User as tmUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password  # Import Django's password hashing function


class TemanUniUserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email', required=True, help_text="Please enter a valid email") 
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = tmUser  # Use your custom user model
        fields = ['email', 'password']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if tmUser.objects.filter(email=email).exists():
            raise ValidationError('This email address is already registered.')
        return email

    def save(self, commit=True, using='temanuni'):
        user = super(TemanUniUserRegistrationForm, self).save(commit=False)

        # Only set the email and password fields
        user.email = self.cleaned_data['email']
        user.password = make_password(self.cleaned_data['password'])  # Hash the password

        if commit:
            user.save(using=using)  # Specify the using parameter to save to a different database

        return user

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True, help_text="Please enter a valid email")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def save(self, commit=True):
        # First, let UserCreationForm handle its own save method to create a User instance
        user = super(UserRegisterForm, self).save(commit=False)

        # Now, create an instance of TemanUniUserRegistrationForm and populate its fields
        temanuni_form = TemanUniUserRegistrationForm({
            'email': self.cleaned_data['email'],
            'password': self.cleaned_data['password1'],  # Use 'password' instead of 'password1'
        })

        if temanuni_form.is_valid():
            # Save user data to the temanuni database using TemanUniUserRegistrationForm
            temanuni_form.save(using='temanuni')

        if commit:
            user.save()

        return user


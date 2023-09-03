from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import TemanUniUserRegistrationForm as tmUserRegistrationForm
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # Success Registration
        if form.is_valid():
            # Create an instance of TemanUniUserRegistrationForm and populate its fields
            tm_user_form = tmUserRegistrationForm({
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password1'],  # Use 'password' instead of 'password1'
            })

            # Save user data to the temanuni database using tmUserRegistrationForm
            tm_user = tm_user_form.save(commit=True)

            messages.success(request, f"You've been successfully registered!")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


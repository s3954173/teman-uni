from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TemanUniUserRegistrationForm as tmUserRegistrationForm
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # Success Registration
        if form.is_valid():
            # Create an instance of TemanUniUserRegistrationForm and populate its fields
            temanuni_form = tmUserRegistrationForm({
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password1'],  # Use 'password' instead of 'password1'
            })
            
            if temanuni_form.is_valid() and temanuni_form.clean_email():
                # Save user data to the temanuni database using temanuni_form
                temanuni_form.save(commit=True)  # Save the data using your custom form

                messages.success(request, f"You've been successfully registered!")
                return redirect('home')
            else:
                messages.success(request, f"Email found, not registered")
                return redirect('home')
            
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import TemanUniUserRegistrationForm as tmUserRegistrationForm
from .forms import UserRegisterForm
from .forms import TemanUniLoginForm as tmLoginForm
from .backends import TemanUniLogin as tmLogin
from django.views.decorators.csrf import csrf_protect



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
                return redirect('login')
            else:
                messages.success(request, f"Email found, not registered")
                return redirect('home')
            
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = tmLoginForm(request.POST)
        if form.is_valid():
            # Get the email and password from the form
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            authenticator = tmLogin()   
        
            # Authenticate the user using your custom authentication backend
            user = authenticator.authenticate(request=request, email=email, password=password)
            
            if user is not None:
                # Set the backend attribute on the user
                user.backend = 'users.backends.TemanUniLogin'

                # Log the user in
                login(request, user)
                messages.success(request, f"You've been successfully logged in!")

                return redirect('home')  # Redirect to the home page or any other page
            else:
                # Authentication failed, show an error message
                form.add_error(None, 'Invalid email or password')
    else:
        form = tmLoginForm()
    
    return render(request, 'users/login.html', {'form': form})


def logout(request):
    # if request.method == 'POST':
    #     form = loginForm(request.POST)
    # else:
    #     form = loginForm()
    return render(request, 'users/logout.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
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

                return redirect('home')
            else:
                messages.error(request, f"This email has already been registered")
                # return redirect('home')
        else:
            messages.error(request, f"Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")

            
    else:
        form = UserRegisterForm()

    error_messages = messages.get_messages(request)    
    return render(request, 'users/register.html', {'form': form, 'error_messages': error_messages})


def login_view(request):
    user = request.user
    if user is not None:
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
                     # Store user_id in the session
                    request.session['user_id'] = user.user_id

                    # Log the user in
                    login(request, user)
                    

                    return redirect('test')  # Redirect to the home page or any other page
                else:
                    # Authentication failed, show an error message
                    messages.error(request, 'Invalid email or password')

        else:
            form = tmLoginForm()

        # Include the error message in the template context
        error_messages = messages.get_messages(request)        
        return render(request, 'users/login.html', {'form': form, 'error_messages': error_messages})
    else:
        return redirect('home')



def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

# Testing Purposes
def test(request):
    if 'user_id' in request.session and request.session['user_id']:
        # The user is authenticated, perform actions accordingly
        # You can also pass 'user' to the template context for use in the template
        return render(request, 'users/test_authenticated.html')
    else:
        # The user is not authenticated, display a different template or message
        return render(request, 'users/test_unauthenticated.html')

def new_login(request):
    return render(request, 'users/login.html')

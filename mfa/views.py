AUTHY_API_KEY = 'tAOR83WIrEwoD7MbVIAsFEM2n1PP60Yd'
from django.shortcuts import render, redirect
from authy.api import AuthyApiClient
from django.http import HttpResponse
from django.template import RequestContext

# Initialize the Authy API client
authy_api = AuthyApiClient(AUTHY_API_KEY)

def mfa(request):
    if request.method == "POST":
        country_code = request.POST.get("country_code")
        phone_number = request.POST.get("phone_number")
        method = request.POST.get("method")

        # Store data in session
        request.session['country_code'] = country_code
        request.session['phone_number'] = phone_number

        # Initiate phone verification
        authy_api.phones.verification_start(phone_number, country_code, via=method)

        # Redirect to the verification page
        return redirect('verify')

    return render(request, "mfa/MFA_input.html")

def verify(request):
    if request.method == "POST":
        token = request.POST.get("token")

        phone_number = request.session.get("phone_number")
        country_code = request.session.get("country_code")

        # Check the verification token
        verification = authy_api.phones.verification_check(phone_number, country_code, token)

        if verification.ok():
            return HttpResponse("<h1>Success!</h1>")

    return render(request, "mfa/verify.html")

    # user = request.user
    # if user is not None:
    #     if request.method == 'POST':
    #         form = tmLoginForm(request.POST)
    #         if form.is_valid():
    #             # Get the email and password from the form
    #             email = form.cleaned_data['email']
    #             password = form.cleaned_data['password']
    #             authenticator = tmLogin()   
            
    #             # Authenticate the user using your custom authentication backend
    #             user = authenticator.authenticate(request=request, email=email, password=password)
                
    #             if user is not None:
    #                 # Set the backend attribute on the user
    #                 user.backend = 'users.backends.TemanUniLogin'
    #                  # Store user_id in the session
    #                 request.session['user_id'] = user.user_id

    #                 # Log the user in
    #                 login(request, user)
                    

    #                 return redirect('home')  # Redirect to the home page or any other page
    #             else:
    #                 # Authentication failed, show an error message
    #                 messages.error(request, 'Invalid email or password')

    #     else:
    #         form = tmLoginForm()

    #     # Include the error message in the template context
    #     error_messages = messages.get_messages(request)        
    #     return render(request, 'mfa/MFA_input.html', {'form': form, 'error_messages': error_messages})
    # else:
    #     return redirect('home')
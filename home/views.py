from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout

def home(request):
    user = request.user
    if 'user_id' in request.session and request.session['user_id']:
        return render(request, 'home/homepage.html')
    else:
        return render(request, 'home/landing.html')


from django.shortcuts import render, redirect
from .models import profile
from .models import languages
from .models import interests
# from .forms import CreateProfile1

def create_profile1(request):
    # submitted = False
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        day = request.POST.get('day')
        month = request.POST.get('month')
        year = request.POST.get('year')
        state = request.POST.get('state')
        city = request.POST.get('city')
        university = request.POST.get('university')
        course = request.POST.get('course')
        language = request.POST.get('language')
        selected_choices = request.POST.getlist('selected_choices')
        if selected_choices:
            selected_choices_str =', '.join(selected_choices)


        date_string = f"{day}-{month}-{year}"
        location_string = f"{state},{city}"

        date_of_birth = date_string
        location = location_string

        profile.objects.create(first_name = first_name, last_name = last_name, gender = gender, 
                               date_of_birth = date_of_birth, location = location, university = university, 
                               course = course)
        languages.objects.create(language = language)
        interests.objects.create(selected_choices = selected_choices_str)
        return redirect('admin/')

        

    return render(request, 'create_profile1.html', {})


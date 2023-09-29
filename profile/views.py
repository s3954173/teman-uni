from django.shortcuts import render, redirect
from temanuni.models import Profile, Interests, Languages, ProfileInterests, ProfileLanguages, User
from .forms import CreateProfile
from django.db.models import Q
import json
from datetime import date

def profile(request):
    # Check user logged in
    if 'user_id' in request.session and request.session['user_id']:
        profile_id = request.session['user_id']  # Retrieve user_id from session
        try:
            profile = Profile.objects.using('temanuni').get(profile_id__user_id=profile_id)
        except Profile.DoesNotExist:
            profile = None
        
        # Render Create Profile Form if profile hasn't been created
        if not profile:
            if request.method == 'POST':
                profile_form = CreateProfile(request.POST)
                # Print the value of the 'dob' field
                print(request.POST.get('dob'))  # Print to console
                if profile_form.is_valid():
                     # Save the form data to the 'temanuni' database
                    profile = profile_form.save(commit=False)
                    profile.profile_id = User.objects.using('temanuni').get(user_id=profile_id)
                    profile.save(using='temanuni')  # Save to the 'temanuni' database

                     # Process and save interests and languages
                    interests_data = profile_form.cleaned_data['interests']
                    languages_data = profile_form.cleaned_data['languages']

                    # Create Interest instances
                    interests = interests_data.split(',')
                    for interest in interests:
                        interest = interest.strip()
                        interest_obj, _ = Interests.objects.using('temanuni').get_or_create(interest=interest)
                        ProfileInterests.objects.using('temanuni').create(profile_id=profile, interest_id=interest_obj)

                    # Create Language instances
                    languages = languages_data.split(',')
                    for language in languages:
                        language = language.strip()
                        language_obj, _ = Languages.objects.using('temanuni').get_or_create(language=language)
                        ProfileLanguages.objects.using('temanuni').create(profile_id=profile, language_id=language_obj)
                                                                                                            

                    return redirect('profile_success')  # Redirect to a success page\
                else:
                    print(profile_form.errors)
            else:
                profile_form = CreateProfile()
            return render(request, 'profile/create_profile.html', {'form': profile_form})
        
        # Render user's profile page if profile found
        else:
            return render(request, 'profile/profile.html')
    else:
        # Redirect home if user not logged in
        return redirect('home')
        
# Delete after testing
def profile_sucess(request):
    return render(request, 'profile/profile_success.html')

        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # gender = request.POST.get('gender')
        # day = request.POST.get('day')
        # month = request.POST.get('month')
        # year = request.POST.get('year')
        # state = request.POST.get('state')
        # city = request.POST.get('city')
        # university = request.POST.get('university')
        # course = request.POST.get('course')
        # language = request.POST.get('language')
        # selected_choices = request.POST.getlist('selected_choices')
        # if selected_choices:
        #     selected_choices_str =', '.join(selected_choices)


        # date_string = f"{day}-{month}-{year}"
        # location_string = f"{state},{city}"

        # date_of_birth = date_string
        # location = location_string

        # profile.objects.create(first_name = first_name, last_name = last_name, gender = gender, 
        #                        date_of_birth = date_of_birth, location = location, university = university, 
        #                        course = course)
        # languages.objects.create(language = language)
        # interests.objects.create(selected_choices = selected_choices_str)
        # return redirect('admin/')

        

   


# Import the models
from temanuni.models import User, Events, Interests, Languages, Messages, EventInvitedUsers, EventUsersDeclined, EventUsersGoing, Photos, Profile, ProfileInterests, ProfileLanguages, Friends

# Query all users from the temanuni database
users = User.objects.using('temanuni').all()

# Query all events from the temanuni database
events = Events.objects.using('temanuni').all()

# Query all interests from the temanuni database
interests = Interests.objects.using('temanuni').all()

# Query all languages from the temanuni database
languages = Languages.objects.using('temanuni').all()

# Query all messages from the temanuni database
messages = Messages.objects.using('temanuni').all()

# Query all invited users for events from the temanuni database
invited_users = EventInvitedUsers.objects.using('temanuni').all()

# Query all users who declined events from the temanuni database
declined_users = EventUsersDeclined.objects.using('temanuni').all()

# Query all users who are going to events from the temanuni database
going_users = EventUsersGoing.objects.using('temanuni').all()

# Query all photos from the temanuni database
photos = Photos.objects.using('temanuni').all()

# Query all profiles from the temanuni database
profiles = Profile.objects.using('temanuni').all()

# Query all profile interests from the temanuni database
profile_interests = ProfileInterests.objects.using('temanuni').all()

# Query all profile languages from the temanuni database
profile_languages = ProfileLanguages.objects.using('temanuni').all()

# Query all friends from the temanuni database
friends = Friends.objects.using('temanuni').all()

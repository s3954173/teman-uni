from django.contrib import admin
from .models import User, Messages, Profile, ProfileInterests, Interests, Languages, EventUsersGoing, EventInvitedUsers, Photos, EventUsersDeclined, Events

admin.site.register(User)
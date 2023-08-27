from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Messages(models.Model):
    message_id = models.BigAutoField(primary_key=True)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message_text = models.TextField()
    timestamp = models.DateTimeField()

class Profile(models.Model):
    profile_id = models.BigAutoField(primary_key=True)
    dob = models.DateField()
    gender = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    course = models.CharField(max_length=255)

class ProfileInterests(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    interest = models.ForeignKey('Interests', on_delete=models.CASCADE)

class Interests(models.Model):
    interest_id = models.PositiveIntegerField(primary_key=True)
    interest = models.CharField(max_length=255)

class Languages(models.Model):
    language_id = models.PositiveIntegerField(primary_key=True)
    language = models.CharField(max_length=255)

class EventUsersGoing(models.Model):
    event = models.ForeignKey('Events', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class EventInvitedUsers(models.Model):
    event = models.ForeignKey('Events', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Photos(models.Model):
    photo_id = models.BigAutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo_filename = models.CharField(max_length=255)
    photo_path = models.CharField(max_length=255)

class EventUsersDeclined(models.Model):
    event = models.ForeignKey('Events', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Events(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    start_date = models.DateField()
    start_time = models.TimeField()
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

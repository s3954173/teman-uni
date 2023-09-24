# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'user'
    

class Events(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    start_date = models.DateField()
    start_time = models.TimeField()
    description = models.TextField()
    creator_id = models.ForeignKey('User', models.DO_NOTHING, db_column='creator_id', related_name='creator_id')

    class Meta:
        managed = False
        db_table = 'events'


class Interests(models.Model):
    interest_id = models.AutoField(primary_key=True)
    interest = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'interests'


class Languages(models.Model):
    language_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'languages'


class Messages(models.Model):
    message_id = models.BigAutoField(primary_key=True)
    sender_id = models.ForeignKey('User', models.DO_NOTHING, db_column='sender_id', related_name='sender_id', related_query_name='sender_id')
    receiver_id = models.ForeignKey('User', models.DO_NOTHING, db_column='receiver_id', related_name='receiver_id', related_query_name='receiver_id')
    message_text = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages'

class EventInvitedUsers(models.Model):
    invited_id = models.BigAutoField(primary_key=True)
    event_id = models.ForeignKey('Events', models.DO_NOTHING, db_column='event_id')
    user_id = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id')

    class Meta:
        managed = False
        db_table = 'event_invited_users'


class EventUsersDeclined(models.Model):
    declined_id = models.BigAutoField(primary_key=True)
    event_id = models.ForeignKey('Events', models.DO_NOTHING, db_column='event_id')
    user_id = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id')

    class Meta:
        managed = False
        db_table = 'event_users_declined'
     


class EventUsersGoing(models.Model):
    going_id = models.BigAutoField(primary_key=True)
    event_id = models.ForeignKey('Events', models.DO_NOTHING, db_column='event_id')
    user_id = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id')

    class Meta:
        managed = False
        db_table = 'event_users_going'
     





class Photos(models.Model):
    photo_id = models.BigAutoField(primary_key=True)
    profile_id = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_id')
    photo_filename = models.CharField(max_length=255)
    photo_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'photos'


class Profile(models.Model):
    profile_id = models.OneToOneField('User', models.DO_NOTHING, primary_key=True, db_column='profile_id', related_name='profile_id')
    dob = models.DateField()
    gender = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    course = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'profile'


class ProfileInterests(models.Model):
    profileinterests_id = models.BigAutoField(primary_key=True)
    profile_id = models.ForeignKey(Profile, models.DO_NOTHING, db_column='profile_id')
    interest_id = models.ForeignKey(Interests, models.DO_NOTHING, db_column='interest_id')

    class Meta:
        managed = False
        db_table = 'profile_interests'


class ProfileLanguages(models.Model):
    profilelanguage_id = models.BigAutoField(primary_key=True)
    profile_id = models.ForeignKey(Profile, models.DO_NOTHING, db_column='profile_id')
    language_id = models.ForeignKey(Languages, models.DO_NOTHING, db_column='language_id')

    class Meta:
        managed = False
        db_table = 'profile_languages'


class Friends(models.Model):
    friends_id = models.BigAutoField(primary_key=True)
    user1_id = models.ForeignKey('User', on_delete=models.CASCADE,  db_column="user1_id", related_name='user1', related_query_name='user1')
    user2_id = models.ForeignKey('User', on_delete=models.CASCADE,  db_column="user2_id", related_name='user2', related_query_name='user2')
    
    # Use IntegerField with choices to represent boolean values
    USER_INTEREST_CHOICES = (
        (0, 'No'),
        (1, 'Yes'),
    )
    user1_interest = models.IntegerField(choices=USER_INTEREST_CHOICES, default=0)
    user2_interest = models.IntegerField(choices=USER_INTEREST_CHOICES, default=0)

    class Meta:
        managed = False
        db_table = 'friends'
     



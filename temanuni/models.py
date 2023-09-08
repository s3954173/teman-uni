# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'
    
    def __str__(self):
        return self.email

class Events(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    start_date = models.DateField()
    start_time = models.TimeField()
    description = models.TextField()
    creator_id = models.ForeignKey('User', models.DO_NOTHING)

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
    sender_id = models.ForeignKey('User', models.DO_NOTHING)
    receiver_id = models.ForeignKey('User', models.DO_NOTHING, related_name='messages_receiver_set')
    message_text = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages'

class EventInvitedUsers(models.Model):
    event_id = models.OneToOneField('Events', models.DO_NOTHING, primary_key=True)  # The composite primary key (event_id, user_id) found, that is not supported. The first column is selected.
    user_id = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_invited_users'
        unique_together = (('event_id', 'user_id'),)


class EventUsersDeclined(models.Model):
    event_id = models.OneToOneField('Events', models.DO_NOTHING, primary_key=True)  # The composite primary key (event_id, user_id) found, that is not supported. The first column is selected.
    user_id = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_users_declined'
        unique_together = (('event_id', 'user_id'),)


class EventUsersGoing(models.Model):
    event_id = models.OneToOneField('Events', models.DO_NOTHING, primary_key=True)  # The composite primary key (event_id, user_id) found, that is not supported. The first column is selected.
    user_id = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_users_going'
        unique_together = (('event_id', 'user_id'),)





class Photos(models.Model):
    photo_id = models.BigAutoField(primary_key=True)
    profile_id = models.ForeignKey('Profile', models.DO_NOTHING)
    photo_filename = models.CharField(max_length=255)
    photo_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'photos'


class Profile(models.Model):
    profile_id = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
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
    profile_id = models.OneToOneField(Profile, models.DO_NOTHING, primary_key=True)  # The composite primary key (profile_id, interest_id) found, that is not supported. The first column is selected.
    interest_id = models.ForeignKey(Interests, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile_interests'
        unique_together = (('profile_id', 'interest_id'),)


class ProfileLanguages(models.Model):
    profile_id = models.OneToOneField(Profile, models.DO_NOTHING, primary_key=True)  # The composite primary key (profile_id, language_id) found, that is not supported. The first column is selected.
    language_id = models.ForeignKey(Languages, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile_languages'
        unique_together = (('profile_id', 'language_id'),)




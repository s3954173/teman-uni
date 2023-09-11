# from django.db import models
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

# # Create your models here.

# def validate_word_limit(value):
#     word_limit = 100
#     words = value.split()
#     if len(words) > word_limit:
#         raise ValidationError(
#             _('Event description cannot exceed %(limit)s words.'),
#             params={'limit':word_limit},
#         )

# class Event(models.Model):
#     eventName = models.CharField(max_length=100)
#     eventDate = models.DateField()
#     eventTime = models.TimeFields()
#     eventDesc = models.TextField(max_length=1000)
#     eventID = models.AutoField(primary_key=True)
#     eventAdmin = models.ForeignKey(on_delete=models.CASCADE)

#     def __str__(self):
#         return self.eventName
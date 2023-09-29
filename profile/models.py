from django.db import models

# Create your models here.

# class profile(models.Model):
#     first_name = models.CharField('first_name', max_length=120)
#     last_name = models.CharField('last_name', max_length=120)
#     gender = models.CharField('gender', max_length=120)
#     date_of_birth = models.CharField('DOB', max_length=120, null=True)
#     location = models.CharField('state', max_length=120)
#     university = models.CharField('university', max_length=120)
#     course = models.CharField('course', max_length=120)
#     def _str_(self):
#         return self.first_name + ' ' + self.last_name

class languages(models.Model):
    language = models.CharField('language', max_length=120)

class interests(models.Model):
    CHOICES = [
        ('being active', 'Being active'),
        ('ambition', 'Ambition'),
        ('confidence', 'Confidence'),
        ('positivity', 'Positivity'),
        ('bls', 'BLS'),
        ('feminismt', 'Feminismt'),
        ('human rights', 'Human Rights'),
        ('environmentalism', 'Environmentalism'),
        ('beaches', 'Beaches'),
        ('camping', 'Camping'),
        ('spa', 'Spa'),
        ('country escape', 'Country Escape'),
        ('romance', 'Romance'),
        ('fantasy', 'Fantasy'),
        ('sci-fi', 'Sci-fi'),
        ('anime', 'Anime')

    ]
    selected_choices = models.CharField(max_length=120, choices=CHOICES)
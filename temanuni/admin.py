from django.contrib import admin
from .models import User as tmUser

#  tmUser.objects.using('temanuni').all()
admin.site.register(tmUser)

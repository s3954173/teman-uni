from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_profile1, name="create_profile1"),
]

#path('<int:day>/<str:month>/<int:year>', views.create_profile1, name="create_profile1"),
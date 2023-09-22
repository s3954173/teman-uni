from django.urls import path
from .import views

urlpatterns = [
    path('EventForm/', views.EventForm, name='events')
]
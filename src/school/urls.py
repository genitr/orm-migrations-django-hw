"""URL configuration for school application."""

from django.urls import path

from .views import students_list


app_name = 'school'

urlpatterns = [
    path('', students_list, name='students'),
]

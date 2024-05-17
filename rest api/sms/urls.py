from django.contrib import admin
from django.urls import path

from sms import views

from .views import *


urlpatterns = [
    path('',views.sendsms,name='sendsms'),
   
]

# if settings.DEBUG:

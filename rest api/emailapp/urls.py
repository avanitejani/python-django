from django.contrib import admin
from django.urls import path

from emailapp import views

from .views import *


urlpatterns = [
    path('',views.sendmail,name='sendmail'),
   
]

# if settings.DEBUG:

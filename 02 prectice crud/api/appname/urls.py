from django.contrib import admin
from django.urls import path
# from appname import views
from .views import *



urlpatterns = [
    path('',DataAPI.as_view())
    
    
]

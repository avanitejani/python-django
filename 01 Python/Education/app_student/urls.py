from django.contrib import admin
from django.urls import path

from app_student import views

# from .views import *
app_name = 'app2'
urlpatterns = [
  
    path('',views.index),
    # path('app1/', views.app1, name='app1'),    

]
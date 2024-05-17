from django.contrib import admin
from django.urls import path

from app_lr import views

# from .views import *

urlpatterns = [
  
    path('',views.index),
    # path('send_request_to_app2/', views.send_request_to_app2, name='send_request_to_app2'),
    

]
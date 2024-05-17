from django.contrib import admin
from django.urls import path
from appsecond import views
# from appsecond import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('ins',views.insert,name='ins'),
    path('delete/<id>',views.delete,name='delete'),
    path('edit/<id>',views.edit,name='edit'),
    
]
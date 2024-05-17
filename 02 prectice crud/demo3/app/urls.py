from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
   path('',views.index,name='index'),
   path('add',views.insert,name='add'),
   path('delete/<id>',views.delete,name='delete'),
   path('edit/<id>',views.edit,name='edit'),




    
]

from django.contrib import admin
from django.urls import path
from .views import *
# from reportcard import views

urlpatterns = [
    path('',index,name="index"),
    path('marks/<id>',marks,name="marks"),
     path('sendstudentmarksemail/<id>',sendstudentmarksemail,name="sendstudentmarksemail")
      # path('search/',views.search,name='search'),
]
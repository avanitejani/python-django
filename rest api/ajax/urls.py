from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("",index,name="index"),
    path("display/",display,name="display"),
    path("adduser",adduser,name="adduser"),
    path("update",update,name="update"),

    
    path("delete/",delete,name="delete"),
    path("edit/",edit,name="edit"),
    path("update",update,name="update"),
    path("search",search,name="search")

    
]
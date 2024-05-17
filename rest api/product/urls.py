from django.contrib import admin
from django.urls import path

from book import views

from .views import *


urlpatterns = [
    path('',views.index),
   
]

# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)
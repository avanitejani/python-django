from django.contrib import admin
from django.urls import path
from  pyment import views
# from .views import *


urlpatterns = [
    
    path('',views.payment,name="payment"),
    path('pay/<amt>',views.pay,name="pay")
   
]


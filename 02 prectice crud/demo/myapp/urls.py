from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('InsertData/',views.InsertData,name='InsertData'),
    path('showpage/',views.showpage,name='show'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('update/<int:pk>',views.updatData,name='update'),
    # path('delete/<int:pk>',views.deleteData,name='delete'),



]



from django.contrib import admin
from django.urls import path
from mysql import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    # is name ke thru is partiqular urls ko call krvana hota hai 
    path('', views.InsertPageView, name='insertpage'),
    path('insert/', views.InsertData, name='insert'),
    path("showpage/", views.ShowPage, name='showpage'),
    path("editpage/<int:pk>", views.EditPage, name='editpage'),
    path("update/<int:pk>", views.UpdataData, name='update'),
    path("delete/<int:pk>", views.DeleteData, name='delete'),



]

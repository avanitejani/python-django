
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('reg',views.reg,name='reg'),
    path('delete/<id>',views.delete,name='delete'),
    path('edit/<id>',views.edit,name='edit'),



    
]

# from django.conf import settings
# from django.conf.urls.static import static

 
# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path



from book import views

from .views import *


urlpatterns = [
    path('',views.index),
    path('books/',BookAPI.as_view(),name='book'),

    # path("book-generic/",BookAPIGeneric1.as_view(),name="bookgeneric"),

    # path("book-generic/<id>",BookAPIGeneric.as_view(),name="bookgeneric1")
]


# Python | Uploading images in Django
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


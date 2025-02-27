"""
URL configuration for restapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('myapp/',include('myapp.urls')),
    # path('',include('myapp.urls')),

    path('book/',include('book.urls')),
    # path('',include('book.urls')),

    path('product/',include('product.urls')),
    # path('',include('product.urls')),

    path('email/',include('emailapp.urls')),
    # path('',include('emailapp.urls')),

    path('pyment/',include('pyment.urls')),
    # path('',include('pyment.urls')),

    path('sms/',include('sms.urls')),
    # path('',include('sms.urls')),

    path('reportcard/',include('reportcard.urls')),
    # path('',include('reportcard.urls')),

    path('ajax/',include('ajax.urls')),
    # path('',include('ajax.urls')),

    # path('reportmail/',include('reportmail.urls')),
    path('',include('reportmail.urls')),



]

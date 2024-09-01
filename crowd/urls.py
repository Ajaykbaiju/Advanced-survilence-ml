"""crowd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first),
    path('index',views.index),
    path('dashboard',views.dashboard),
    path('login/',views.login),
    path('addlogin',views.addlogin),
    path('logout/',views.logout),
    path('register/',views.register),
    path('addregister',views.addregister),
    path('cam1',views.cam1),
    path('cam2',views.cam2),
    path('cam3',views.cam3),
    path('start_abnormal_activity',views.start_abnormal_activity),
    path('start_tracking',views.start_tracking),
 
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

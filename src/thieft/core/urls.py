from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.front),
    path('signin', views.front),
    path('profile', views.front),
    path('settings', views.front),
    path('vehicle', views.front),
    path('help', views.front),
    path('location', views.front),
    path('changepassword', views.front),
    path('changeusername', views.front),
    path('devices', views.front),
    path('accessibility', views.front),
    path('alerts', views.front),
    path('data', views.front),
    path('security', views.front),
    path('incidents', views.front),
    path('account', views.front),
    path('tutorial', views.front),
]
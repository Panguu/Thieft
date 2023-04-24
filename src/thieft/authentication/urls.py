from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('auth/users/', views.getUsers),
    path('auth/login/', views.loginUser),
    path('auth/createUser/<str:user_id>', views.createUser),
    path('auth/removeUser/<str:user_id>', views.removeUser),
    path('auth/changeUsername/', views.changeUsername),
    path('auth/changePassword/', views.changePassword),
    path('auth/logout/', views.logoutUser),
    path('auth/checkToken/', views.checkToken),
    path('auth/profileDetails/', views.getProfileDetails),
    path('auth/updateProfileDetails/', views.updateProfileDetails),
]

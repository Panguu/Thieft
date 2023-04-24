from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('tracking/data/<str:device_id>/<int:journey_id>', views.getJourneyInfo),
    path('tracking/data/post/', views.postJourneyInfo),
    path('tracking/data/createJourney/', views.createJourney),
    path('tracking/data/getAllJourneys/', views.getAllJourneysForDevice),
    path('tracking/getJourneyInfo/', views.getjourneyLocation),
]
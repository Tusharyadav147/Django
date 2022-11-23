from django.contrib import admin
from django.urls import path
from .views import signup, signin, viewcar, addcar, carbooked

urlpatterns = [
    path("signup/", signup),
    path("signin/", signin),
    path("addcar/", addcar),
    path("viewcar/", viewcar),
    path("booked/", carbooked),
]

from django.contrib import admin
from django.urls import path
from .views import signup, signin, viewcar, addcar, carbooked, car_entry, calculatetime

urlpatterns = [
    path("signup/", signup),
    path("signin/", signin),
    path("addcar/", addcar),
    path("viewcar/", viewcar, name = "viewcar1"),
    path("viewcar/<str:pk>", viewcar, name = "viewcar"),
    path("booked/", carbooked),
    path("showroom/", car_entry),
    path("timecount/", calculatetime)
]

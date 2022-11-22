from django.contrib import admin
from django.urls import path
from .views import signup, signin, viewcar, addcar, price, prices, all

urlpatterns = [
    path("signup/", signup),
    path("signin/", signin),
    path("addcar/", addcar),
    path("viewcar/", viewcar),
    path("viewcar/price/<str:car>", price),
    path("viewcar/price/", price),
    path("addcar/prices/", prices),
    path("all/", all)
]

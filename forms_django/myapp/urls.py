from django.urls import path
from .views import home_view, myform, view_data

urlpatterns = [
    path("forms/", home_view),
    path("myform/", myform ),
    path("data/", view_data)
]
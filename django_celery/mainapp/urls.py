
from django.contrib import admin
from django.urls import path, include
from .views import test, GenerateRandomUserView, viewusers, send_mail_to_all, schedule_mail

urlpatterns = [
    path('test/', test),
    path("user/", GenerateRandomUserView),
    path("viewuser/", viewusers),
    path("sendmail/", send_mail_to_all),
    path("schedule/", schedule_mail)
]
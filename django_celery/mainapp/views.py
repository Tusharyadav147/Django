from django.shortcuts import render
from .tasks import test_func, create_random_user_accounts
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serializer import UserSerializer
from .tasks import send_email_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

# Create your views here.
@api_view(["GET", "POST"])
def test(request):
    test_func.delay()
    return Response("Done")

@api_view(["POST"])
def GenerateRandomUserView(request):
    if request.method == "POST":
        print(request.data)
        create_random_user_accounts.delay(request.data["total"])
        return Response("Done")

@api_view(["GET"])
def viewusers(request):
    if request.method == "GET":
        all_users = get_user_model().objects.all()
        serializer = UserSerializer(all_users, many = True)

        return Response(serializer.data)

@api_view(["GET"])    
def send_mail_to_all(request):
    send_email_func.delay()
    return Response("Done")

@api_view(["GET"])
def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour =1, minute = 10)
    task = PeriodicTask.objects.create(crontab = schedule, name = "schedule_mail_task_"+ "1", task= "mainapp.task.send_email_func", args = json.dumps((2,3,)))
    return Response("Done")

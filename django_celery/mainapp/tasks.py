from celery import shared_task
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import string
from .serializer import UserSerializer
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django_celery import settings

@shared_task(bind = True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"

@shared_task
def create_random_user_accounts(total):
    for i in range(int(total)):
        username = "user_{}".format(get_random_string(10, string.ascii_letters))
        email = "{}@gmail.com".format(username)
        password = get_random_string(50)
        data = User.objects.create_user(username=username, email=email, password=password)
        print(data)
        data.save()
    return "{} random users created with success".format(int(total))

@shared_task(bind = True)
def send_email_func(self):
    users = ["tusharsonp303@gmail.com", "hjain4605@gmail.com"]
    for user in users:
        mail_subject = "Test Model"
        message = "Don't need to response back"
        to_email = user
        send_mail(
            subject=mail_subject,
            message=message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"


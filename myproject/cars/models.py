from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=14)  
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class LogIn_Wrong(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

class CarDetails(models.Model):
    car_name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    model_year = models.IntegerField()
    price = models.IntegerField(default=200000)

    def __str__(self):
        return self.car_name

payment = (
    ("Cash","Cash"),
    ("Check","Check"),
)

class CarBook(models.Model):
    person = models.ForeignKey(Register, on_delete=models.CASCADE)
    car = models.ForeignKey(CarDetails, on_delete=models.CASCADE, default="dh")
    purchase_date = models.DateField()
    payment_mode= models.CharField(max_length=6,choices=payment, default="None")
    
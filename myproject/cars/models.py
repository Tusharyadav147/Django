from django.db import models

# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=14)  
    password = models.CharField(max_length=20)

class LogIn_Wrong(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

class CarDetails(models.Model):
    car_name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    model_year = models.IntegerField()

class CarPrice(models.Model):
    car_details = models.OneToOneField(CarDetails, on_delete=models.CASCADE, primary_key=True)
    price = models.IntegerField()


    

from django.db import models

# Create your models here.
class MyModel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    roll_no = models.IntegerField(help_text="Enter Your roll Number")
    password = models.CharField(max_length=200)

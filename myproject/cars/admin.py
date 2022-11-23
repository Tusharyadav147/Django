from django.contrib import admin
from .models import Register, LogIn_Wrong, CarDetails, CarBook

# Register your models here.

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    pass

@admin.register(LogIn_Wrong)
class LogInAdmin(admin.ModelAdmin):
    pass

@admin.register(CarDetails)
class CarDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(CarBook)
class CarBookAdmin(admin.ModelAdmin):
    pass
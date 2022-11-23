from django.contrib import admin
from .models import Register, LogIn_Wrong, CarDetails, CarBook, CarShowRoomInOut
from django.db.models import Sum
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

# Register your models here.

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "show_total", "no_cars_pur")

    def show_total(self, obj):
        result = CarBook.objects.filter(person__first_name = obj).aggregate(Sum("car__price"))
        print(obj)
        return result["car__price__sum"]

    def no_cars_pur(self, obj): 
        count = CarBook.objects.filter(person__first_name = obj)
        print(count.values())
        url = (
            reverse("viewcar", args=[count.values()[0]["person_id"]])
        )
        print(count.values()[0]["person_id"])
        return  format_html('<a href="{}">{} Cars</a>', url, count.count())
    no_cars_pur.short_description = "No. Cars Purchase"

@admin.register(LogIn_Wrong)
class LogInAdmin(admin.ModelAdmin):
    pass

@admin.register(CarDetails)
class CarDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(CarBook)
class CarBookAdmin(admin.ModelAdmin):
    pass

@admin.register(CarShowRoomInOut)
class CarShowRoomInOutAdmin(admin.ModelAdmin):
    pass
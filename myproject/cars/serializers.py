from rest_framework import serializers
from .models import Register, LogIn_Wrong, CarDetails, CarPrice

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = "__all__"

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogIn_Wrong
        fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    car_name = serializers.CharField(max_length= 20)
    class Meta:
        model = CarDetails
        fields = "__all__"

class PriceSerializer(serializers.ModelSerializer):
    car_details_id = serializers.CharField(max_length= 20)
    class Meta:
        model = CarPrice
        fields = "__all__"



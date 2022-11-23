from rest_framework import serializers
from .models import Register, LogIn_Wrong, CarDetails, CarBook, CarShowRoomInOut

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

class CarBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarBook
        depth = 1
        fields = "__all__"

class ShowRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarShowRoomInOut
        depth = 1
        fields = "__all__"


from rest_framework import serializers
from .models import MyModel

class MySerializer(serializers.ModelSerializer):

    class Meta:
        model = MyModel
        fields = ["first_name", "last_name", "roll_no", "password"]
        labels = {"first_name": "First", "last_name": "last", "roll_no": "Roll", "password": "Pass"}
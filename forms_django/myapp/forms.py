from django import forms
from .models import MyModel

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required = False)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())
    
class MyForm(forms.ModelForm):

    class Meta:
        model = MyModel
        fields = ["first_name", "last_name", "roll_no", "password"]
        labels = {"first_name": "First", "last_name": "last", "roll_no": "Roll", "password": "Pass"}

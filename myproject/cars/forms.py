from django import forms
from .models import Register, LogIn_Wrong

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required = False)
    email = forms.EmailInput()
    mobile = forms.CharField(max_length=14)
    password = forms.CharField(widget = forms.PasswordInput())
    
    class Meta:
        model = Register
        fields = "__all__"

class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = LogIn_Wrong
        fields = "__all__"


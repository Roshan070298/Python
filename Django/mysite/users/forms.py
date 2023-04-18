from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    #Meta class is a class that provides information about the class itself.
    #  here the meta class holds info about the registerForm class

    class Meta:
        model=User #the form(RegisterForm) belongs to the user model 
        fields=['username','email','password1','password2']
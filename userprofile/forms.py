from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import EmployeeProfile
from django import forms
from django.forms import ModelForm

from home import models

class EmployerSignupForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    first_name = forms.CharField(max_length=50, required=True)
    # last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username','first_name', 'email','is_staff', 'password1', 'password2']



class EmployeeSignupForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']


class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['first_name', 'last_name', 'phone', 'email']



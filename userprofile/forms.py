from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm





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



# class ApplicantForm(forms.ModelForm):
#     class Meta:
#         model = Applicant
#         fields = ['username','first_name','last_name','gender','email', 'cover_letter','resume','job_title', 'job_location', 'salary']
#         widgets = {
#             'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'username'}),
#             'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'first_name'}),
#             'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'last_name'}),
#             'gender': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'gender'}),
#             'email': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'email'}),
#             'job_title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'job_title'}),
#             'job_location': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'job_location'}),
#             'salary': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'salary'}),
#             'cover_letter': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Cover Letter'}),
#             'resume': forms.FileInput(attrs={'class':'form-control', 'placeholder': 'Upload CV'}),
#         }






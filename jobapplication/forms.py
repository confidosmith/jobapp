from django import forms
# from django.forms import ModelForm
from django.forms import Form
# from .models import Applicantion

# class ApplicantForm(forms.Form):
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
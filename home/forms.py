from django import forms 
from .models import *



class ListjobForm(forms.ModelForm):
    class Meta:
        model = Listjob
        fields = ['job_title', 'job_location','category', 'salary', 'description','tags','deadline','website','logo']
        widgets = {
            'job_title': forms.TextInput(attrs={'class':'form-control'}),
            'job_location': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'salary': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'tags': forms.TextInput(attrs={'class':'form-control'}),
            'deadline': forms.DateInput(attrs={'class':'form-control'}),
            'website': forms.TextInput(attrs={'class':'form-control'}),
            'logo': forms.FileInput(attrs={'class':'form-control'}),
        }


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['listjob','employer','first_name','last_name','email', 'cover_letter','resume', 'job_location', 'salary']
        widgets = {
            'listjob': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Job Title'}),
            'employer': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Employer'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'last_name'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'email'}),
            'job_location': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'job_location'}),
            'salary': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'salary'}),
            'cover_letter': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Cover Letter'}),
            'resume': forms.FileInput(attrs={'class':'form-control', 'placeholder': 'Upload CV'}),
        }



from django import forms
from myproject.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class contactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
	fields = ['name', 'email', 'mobile','message']
        

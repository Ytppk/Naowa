from django.core import validators
from django import forms
from .models import Members

class MemReg(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['category', 'name', 'slug', 'husbandname', 'rank', 'appointment', 'phone', 'email','address', 'dob', 'image']

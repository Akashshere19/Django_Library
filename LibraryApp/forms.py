from django.core import validators
from django import forms
from .models import BookRecord

class BookRegistration(forms.ModelForm):
    class Meta:
        model=BookRecord
        fields=['BookName','OutDate','InDate','UserName','MobNo']
        widget={
            'BookName': forms.TextInput(attrs={'class':'form-control'}),
            'OutDate': forms.DateInput(attrs={'class':'form-control'}),
            'InDate': forms.DateInput(attrs={'class':'form-control'}),
            'UserName': forms.TextInput(attrs={'class':'form-control'}),
            'MobNo': forms.TextInput(attrs={'class':'form-control'}),
        }

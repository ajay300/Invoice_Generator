from django import forms
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.forms import UserCreationForm

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'password' ]

        labels = {
            'password':'Enter Password',
            # 'password2':'Confirm Pasword',
        }
        
        widgets = {
            'username':forms.TextInput(attrs={
                'class':'form-control'
            }),
            
            'password':forms.PasswordInput(attrs={
                'class':'form-control'
            }),
            
        }


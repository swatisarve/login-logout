from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Myusers(UserCreationForm):
    first_name=forms.CharField(max_length=101)
    last_name=forms.CharField(max_length=101)
    emailid=forms.CharField(max_length=101)
    mobilenumber=forms.CharField(max_length=101)
    gender=forms.CharField(max_length=101)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','emailid','mobilenumber','gender','password1','password2']

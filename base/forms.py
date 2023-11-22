from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class AddMembersModelForm(ModelForm):
    class Meta:
        model = Members
        fields = ['id','firstname','lastname','email','division','phonenumber',]
        

class PostNewsModelForm(ModelForm):
    class Meta:
        model = PostNews
        fields = ['texttopost', 'title']
        
class ApplicantModelForm(ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'    
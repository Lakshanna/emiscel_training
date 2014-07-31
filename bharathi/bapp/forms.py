from django import forms
from bapp.models import Userprofile,student
from django.contrib.auth.models import User


class Userform(forms.ModelForm):
 	password=forms.CharField(widget=forms.PasswordInput())
  	class Meta:
  		model=User
  		fields=('username','email','password')

class UserProfileform(forms.ModelForm):
  	class Meta:
  		model=Userprofile
  		fields=('company','website')


class myform(forms.ModelForm):
  	class Meta:
  		model=student




from django import forms
from sivaapp.models import Signup,Student
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model=User
		fields=('username','email','password')

class SignupForm(forms.ModelForm):
	
	class Meta:
		model=Signup



class StudentForm(forms.ModelForm):
	class Meta:
		model=Student


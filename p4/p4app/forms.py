from django import forms
from p4app.models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(max_length=60, widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = Userprofile
		fields = ('school','district')

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student

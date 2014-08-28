from django import forms
from django.contrib.auth.models import User
from myapp.models import stud_details, UserProfile

class MyModelForm(forms.ModelForm):
	class Meta:
		model=stud_details

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username','email','password')
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('company','website')
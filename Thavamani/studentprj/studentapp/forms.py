from django import forms
from studentapp.models import *
# class loginform(forms.ModelForm):
# 	class Meta:
# 		model=login

class studentform(forms.ModelForm):
	class Meta:
		model=studenttable
		exclude={"total"}

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('company', 'website')

# class UserForm1(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput())
# 	class Meta:
# 		model = User
# 		fields = ('username', 'password')
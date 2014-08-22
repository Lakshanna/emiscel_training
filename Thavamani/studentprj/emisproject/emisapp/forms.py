from django import forms
from emisapp.models import *
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('company', 'website')	
class studentform(forms.ModelForm):
	class Meta:
		model=studenttable
		
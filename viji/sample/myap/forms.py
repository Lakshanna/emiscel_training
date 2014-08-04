from django import forms
from django.contrib.auth.models import User
from myap.models import student, UserProfile 

class MyModelForm(forms.ModelForm):
#	sexradio = forms.RadioSelect(choices=[('M', 'Male'), ('F','Female')])
	class Meta:
		model = student
		exclude = ('total',)
		widgets = {'sex': forms.RadioSelect }
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username','email','password')
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('company','website')

#class myform(forms.Form):


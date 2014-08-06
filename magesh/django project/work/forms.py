from django import forms
from work.models import *
from django.contrib.auth.models import User


class MyForm(forms.ModelForm):
	class Meta:
		model=student
		
class stdform(forms.ModelForm):
	class Meta:
		model=student

# class UserForm(forms.ModelForm):
# 	#password=forms.CharField(widget=forms.passwordinput())
# 	class Meta:
# 		model=User
# 		fields=('username,email,password')
	
# class UserProfileForm(forms.ModelForm):
# 	class Meta:
# 		model=profile
# 		fields=('firm,web')
# class teacherform(forms.ModelForm):
# 	class Meta:
# 		model=teacher

		
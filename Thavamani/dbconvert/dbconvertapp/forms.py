from django import forms
from dbconvertapp.models import *
class DisplayForm(forms.ModelForm):
	class Meta:
		model = Schoollist
	# fields = ('username', 'email', 'password')
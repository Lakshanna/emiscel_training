from django import forms
from myapp.models import sdetails

class MyForm(forms.ModelForm):
	class Meta:
		model=sdetails
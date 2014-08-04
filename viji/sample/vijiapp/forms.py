from django import forms
from vijiapp.models import student_details

class StudentForm(forms.ModelForm):
	class Meta:
		model = student_details

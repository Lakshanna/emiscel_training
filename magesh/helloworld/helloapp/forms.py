from django import forms
class MyForm(forms.Form):
	roll_no=forms.IntegerField()
	admin_dt=forms.DateField()
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=True)
	is_spl_stu=forms.BooleanField()
	photo=forms.FileField()
	email=forms.EmailField()



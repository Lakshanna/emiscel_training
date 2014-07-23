from django.shortcuts import render
from django.views.generic import View
from myapp.forms import StudentForm
from myapp.models import student_details 

class Student_detailCreateView(View):
	def get(self,request,**kwargs):
		form = StudentForm()
		return render(request,'add.html',{'form_details':form})

	def post(self,request,**kwargs);
		return render(request,'add.html',{'form_details':form})
		
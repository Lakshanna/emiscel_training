from django.shortcuts import render
from django.views.generic import View
from myapp.forms import StudentForm
from myapp.models import student_details 

class Student_detailCreateView(View):
	def get(self,request,**kwargs):
		form = StudentForm()
		return render(request,'add.html',{'form_details':form})

	def post(self,request,**kwargs):
		form = StudentForm(request.POST)
		if form.is_valid():
			student = student_details(
				uid = form.cleaned_data['uid'],
				name = form.cleaned_data['name'],
				gender = form.cleaned_data['gender'],
				mother_tongue = form.cleaned_data['mother_tongue'],
				nationality = form.cleaned_data['nationality'],
				)
			student.save()
			student_list = student_details.objects.all()
		return render(request,'view.html',{'student_list':student_list})


class Student_detailUpdateView(View):
	def get(self,request,**kwargs):
		pk = self.kwargs.get('pk')
		instance = student_details.objects.get(uid=pk)
		return render(request,'edit.html',{'form_details':instance,'pk1':pk})

	def post(self,request,**kwargs):
		pk=self.kwargs.get('pk')
		form = StudentForm(request.POST)
		if form.is_valid():
			student_data = student_details.objects.get(uid=pk)
			student_data.uid = form.cleaned_data['uid']
			student_data.name = form.cleaned_data['name']
			student_data.gender = form.cleaned_data['gender']
			student_data.mother_tongue = form.cleaned_data['mother_tongue']
			student_data.nationality = form.cleaned_data['nationality']
			student_data.save()
			student_list = student_details.objects.get(uid=pk)
		return render(request,'view.html',{'student_list':student_list, 'pk':pk})

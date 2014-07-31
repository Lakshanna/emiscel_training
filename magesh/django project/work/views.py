from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from work.models import *
from work.forms import *
from django.views.generic import View
# Create your views here.

class home(View):
	def get(self,request):
		return render(request,"index.html",locals())
	def post(self,request):
		return render(request,"index.html",locals())


class new_entry(View):
	def get(self,request,**kwargs):
		a=MyForm()
		# dist = district.objects.order_by("id")
		# bloc = block.objects.order_by("id")
		# sch = school.objects.order_by("id")
		# std = standard.objects.order_by("id")
		return render(request,"new_entry.html",locals())

	def post(self,request,**kwargs):
		a=MyForm(request.POST)
		if a.is_valid():
			a=student(
				roll_no=a.cleaned_data['roll_no'],
				name=a.cleaned_data['name'],
				std=a.cleaned_data['std'],
				school=a.cleaned_data['school'],
				block=a.cleaned_data['block'],
				district=a.cleaned_data['district'],
				marks=a.cleaned_data['marks'],
				)
			a.save()
		return HttpResponseRedirect('/entry')	

class new_view(View):
	def get(self,request,**kwargs):
		b = student.objects.order_by("roll_no")
		return render(request,"new_view.html",locals())

	def post(self,request,**kwargs):
		return render(request,"new_view.html",locals())




class new_edit(View):
	def get(self,request,**kwargs):
	 dist = district.objects.order_by("id")
	 bloc = block.objects.order_by("id")
	 sch = school.objects.order_by("id")
	 std = standard.objects.order_by("id")
	 form=MyForm(request.POST)
	 sid=kwargs.get("sid")
	 a=student.objects.get(id=sid)
	 return render(request,"new_edit.html",locals())
	
	def post(self,request,**kwargs):
		sid=kwargs.get("sid")
		if request.POST:
			  st=standard.objects.get(std=request.POST['std'])
			  sc=school.objects.get(school=request.POST['school'])
			  blo=block.objects.get(block=request.POST['block'])
			  dis=district.objects.get(district=request.POST['district'])
			  a=student(
			  	id=sid,
			  	roll_no=request.POST['roll_no'],
			  	name=request.POST['name'],
			  	std=st,
			  	school=sc,
			  	block=blo,
			  	district=dis,
			  	marks=request.POST['mark'],)
			  a.save()
			  return HttpResponseRedirect('/view')
		

class stdentry(View):
 def get(self,request):
  a=stdform()
  return render(request,"std.html",locals())
	
 def post(self,request):
	a=stdform(request.POST)
	if a.is_valid():
			a=student(
				roll_no=a.cleaned_data['roll_no'],
				name=a.cleaned_data['name'],
				std=a.cleaned_data['std'],
				school=a.cleaned_data['school'],
				block=a.cleaned_data['block'],
				district=a.cleaned_data['district'],
				marks=a.cleaned_data['marks'],
				)
			a.save()
	return render(request,"std.html",locals())
	
class new_delete(View):
  	def get(self,request,**kwargs):
  		sid=kwargs.get("bid")
  		a=student.objects.get(id=sid)
  		return render(request,"new_delete.html",locals())
  		

  	def post(self,request,**kwargs):
 	  	sid=kwargs.get("bid")
 	  	a=student.objects.get(id=sid)
 	  	a.delete()	
 		return HttpResponseRedirect('/view')
		


	

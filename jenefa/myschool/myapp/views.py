from django.shortcuts import render,redirect, render_to_response
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from myapp.forms import MyForm
from myapp.models import *

def home(request):
	return render(request,'home.html',locals())

def stud_view(request):
	stud_list=sdetails.objects.all()
	return render(request,'stud_view.html',locals())

class stud_entry(View):
	# import ipdb; ipdb.set_trace()
	def get(self,request,**kwargs):
		import ipdb; ipdb.set_trace()
		form_details=MyForm()
		return render(request,"entry.html",locals())

	def post (self,request,**kwargs):
		import ipdb; ipdb.set_trace()
		form=MyForm(request.POST)
		if form.is_valid():
			newentry=sdetails(
				S_ID=form.cleaned_data['S_ID'],
				Name=form.cleaned_data['Name'],
				Sex=form.cleaned_data['Sex'],
				Std=form.cleaned_data['Std'],
				School=form.cleaned_data['School'],
				)
			newentry.save()
			stud_list=sdetails.objects.all()
			return render(request,"stud_view.html",locals())
				
				



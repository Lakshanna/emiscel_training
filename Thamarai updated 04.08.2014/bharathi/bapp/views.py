from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from bapp.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.shortcuts import render 
from bapp.models import *
from django.http import HttpResponseRedirect,HttpResponse
from bapp.forms import *
import ipdb
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import render

# Create your views here.

def signup(request):
 		if request.method == 'POST':
			form=Userform
 			user_form=Userform(data=request.POST)
 			profile_form=UserProfileform(data=request.POST)
 			if user_form.is_valid()and profile_form.is_valid(): 
 				user=user_form.save()
 				user.set_password(user.password)
 				user.save()
 				profile=profile_form.save(commit=False)
				profile.user=user
 				profile.save()
			return render(request,'submit.html',locals())
		else:
		 	a=Userform()
		 	b=UserProfileform()
		 	return render(request,'userform.html',locals())


def userlogin(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password,)
		if user:
			if user.is_active:
				login(request,user)
				request.session['login']= 'Emis'
				return HttpResponseRedirect('/home')
			else:
				return HttpResponse("your EMIS account is disabled")
		else:
			return HttpResponse("invalid login details suplied")
	return render(request,"login.html",locals())


@login_required
def home(request):
	return render(request,"home.html",locals())


@login_required
def userlogout(request):
	logout(request)
	return HttpResponseRedirect('/login')


class entry(View):
	def get(self,request,**kwargs):
		form= myform()
		a=studying.objects.all()
		return render(request,'entry.html',locals())

	def post(self,request,**kwargs):
		form=myform(request.POST)
		if form.is_valid():
			if request.POST:
				newentry=student(uid = request.POST['uid'],
				name = form.cleaned_data['name'],
				fname = form.cleaned_data['fname'],
				school = form.cleaned_data['school'],
				std = form.cleaned_data['std'],
				tam = form.cleaned_data['tam'],
				eng = form.cleaned_data['eng'],
				mat = form.cleaned_data['mat'],
				phy = form.cleaned_data['phy'],
				chem = form.cleaned_data['chem'],
				bio = form.cleaned_data['bio'],
				tot = form.cleaned_data['tot'],

				)
			
				newentry.save()
			adeddata= student.objects.all()
			return render(request,'view.html',{'adeddatas':adeddata,})



class edit(View):
	def get(self,request,**kwargs):
		pk = self.kwargs.get('pk')
		a=studying.objects.all()
		instance= student.objects.get(uid=pk)
		return render(request,'edit.html',{'instances':instance,'pk1':pk,'a':a},)

	def post(self,request,**kwargs):
		pk=self.kwargs.get('pk')
		form=myform(request.POST)
		a=studying.objects.all()
		if form.is_valid():
			details_update= student.objects.get(uid=pk)
			details_update.uid = form.cleaned_data['uid']
			details_update.name = form.cleaned_data['name']
			details_update.fname = form.cleaned_data['fname']
			details_update.school = form.cleaned_data['school']
			details_update.std = form.cleaned_data['std']
			details_update.tam = form.cleaned_data['tam']
			details_update.eng = form.cleaned_data['eng']
			details_update.mat = form.cleaned_data['mat']
			details_update.phy = form.cleaned_data['phy']
			details_update.chem = form.cleaned_data['chem']
			details_update.bio = form.cleaned_data['bio']
			details_update.tot = form.cleaned_data['tot']
			details_update.save()
		else:
			return render(request,'edit.html',{'form':form,'a':a})
		adeddata= student.objects.get(uid=pk)
		return render(request,'view.html',{'adeddatas':adeddata,'pk':pk})

		
			

class view(View):
	def get(self,request,**kwargs):
		adeddata = student.objects.all()
		return render(request,'view.html',{'adeddatas':adeddata,})
	def post(self,request,**kwargs):
		adeddata= student.objects.all()
		return render(request,'view.html',{'adeddatas':adeddata,})


class markview(View):
	def get(self,request,**kwargs):
		b = student.objects.all().order_by('-tot')
		return render(request,'markview.html',{'bs':b,})
	def post(self,request,**kwargs):
		b = student.objects.all().order_by('-tot')
		return render(request,'markview.html',{'bs':b,})


class classview(View):
	def get(self,request,**kwargs):
		b = student.objects.all().order_by('std')
		return render(request,'classview.html',{'bs':b,})
	def post(self,request,**kwargs):
		b = student.objects.all().order_by('std')
		return render(request,'classview.html',{'bs':b,})



class delete(View):
	def get(self,request,**kwargs):
		pk = self.kwargs.get('pk')
		instance= student.objects.get(uid=pk)
		return render(request,'delete.html',{'instances':instance,'pk1':pk},)

	def post(self,request,**kwargs):
		pk=self.kwargs.get('pk')
		datadelete= student.objects.get(uid=pk)
		datadelete.delete()
		#adeddata= student.objects.get(uid=pk)
		return HttpResponse('YOUR DATA DELETED SUCCESFULLY')
		return HttpResponseRedirect('/view/')	
		


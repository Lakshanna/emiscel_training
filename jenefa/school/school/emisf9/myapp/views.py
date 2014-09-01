from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib import admin
from django import forms
from myapp.models import *
from myapp.forms import MyModelForm
from myapp.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.template import RequestContext
# Create your views here.

def home(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		request.session['uname']=username
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return render(request, 'emismain.html',locals())
			else:
				return HttpResponse("Your Account is disabled")
		else:
			return HttpResponse("Invalid login details")
	return render(request, 'home.html', locals())

def loging(request):
	if request.method == 'GET':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			return HttpResponseRedirect('/') 
		else:
			a=UserForm()
			b=UserProfileForm()
	return render(request, 'register.html', locals())



@login_required
def logot(request):
	logout(request)
	return render(request, 'home.html', locals())

def log(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return render(request, 'logsuccess.html',locals())
			else:
				return HttpResponse("Your Account is disabled")
		else:
			return HttpResponse("Invalid login details supplied")
	return render(request, 'log.html', locals())



@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text")

@login_required
def logsuccess(request):
	return render(request,'logsuccess.html',locals())



class entry(View):
	def get(self,request,**kwargs):
		a=MyModelForm()
		return render(request,"entry.html",locals())

	def post(self,request,**kwargs):
		# import ipdb
		# ipdb.set_trace()
		form =MyModelForm(request.POST)
		if form.is_valid():
			newentry=stud_details(
				Name=form.cleaned_data['Name'],
				Std=form.cleaned_data['Std'],
				Sex=form.cleaned_data['Sex'],
				Dob=form.cleaned_data['Dob'],
				Medium=form.cleaned_data['Medium'],
				Mother_tongue=form.cleaned_data['Mother_tongue'],
				Community=form.cleaned_data['Community'],
				Religion=form.cleaned_data['Religion'],
				District=form.cleaned_data['District'],
				Phone_no=form.cleaned_data['Phone_no'],
				Address=form.cleaned_data['Address'],
				Pin_code=form.cleaned_data['Pin_code'],
				)
			newentry.save()
		slist=stud_details.objects.all()
		return render(request,"view.html",locals())



# class delete(View):



	
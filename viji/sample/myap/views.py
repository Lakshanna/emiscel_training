from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect 
from django import forms
from myap.models import *
from myap.forms import MyModelForm
from myap.forms import UserForm, UserProfileForm
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
			return HttpResponse("Invalid login details supplied")
	return render(request, 'home.html', locals())

def loging(request):
	if request.method == 'POST':
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

class entscr(View):
	def get(self,request,**kwargs):
		uname = request.session['uname']
		a = MyModelForm()
		return render(request, 'entscr.html', locals())
	def post(self,request,**kwargs):
		# import ipdb;ipdb.set_trace()
		form = MyModelForm(request.POST, request.FILES)
 		if form.is_valid():
 			sp = form.cleaned_data['splchi']
			if sp == True:
				sp = True
			else:
				sp =  False
			email = form.cleaned_data['email'],
			splchi = "True",
			photo = form.cleaned_data['photo'],
 			a=student (
 				studid = form.cleaned_data['studid'],
 			 	name = form.cleaned_data['name'],
 			 	fname = form.cleaned_data['fname'],
 			 	age = form.cleaned_data['age'],
 			 	std = form.cleaned_data['std'],
 			 	sex = form.cleaned_data['sex'],
 			 	splchi = sp,
 			 	photo = form.cleaned_data['photo'],
				email = form.cleaned_data['email'],
				phys = form.cleaned_data['phys'],
				chem = form.cleaned_data['chem'],
				math = form.cleaned_data['math'],
				lang = form.cleaned_data['lang'],
				total = form.cleaned_data['phys'] + form.cleaned_data['chem'] + form.cleaned_data['math'] +form.cleaned_data['lang']
				)
			a.save()
			b=student.objects.all()
			request.session["username"]="username"
			return render(request, 'entscr.html', locals())
		else:
			return render(request, 'entscr.html', locals())

def viewscr(request):
	uname = request.session['uname']
	b = student.objects.all()
	return render(request,'viewstud.html',locals())

@login_required
def logot(request):
	logout(request)
	return render(request, 'home.html', locals())




#	import ipdb ; ipdb.set_trace()


		




def post_form_upload(request):
	if request.method == 'GET':
		form = MyModelForm()
	else:
		form = MyModelForm(request.POST)
	if form.is_valid():
		name=form.cleaned_data('name')
		fname = form.cleaned_data('fname')
		return HttpResponseRedirect(reverse('post_detail',kwargs={'post_id:post.id'}))










def entry(request):
	if request.POST:
		# import ipdb
		# ipdb.set_trace()
		name = request.POST['name']
		fname = request.POST['fname']
		age = request.POST['age']
		sex = request.POST['sex']
		sp = request.POST.get('splchi', False)

#		if request.POST['splchi'] == "on":
#			sp=True
#		else:
#			sp=False
#		photo = request.FILES['photo']
		email = request.POST['email']
		a = student (name=name, fname = fname, age=age, sex=sex, splchi=sp, email=email)
		a.save()

	b=student.objects.all()
	return render(request, 'entry.html', locals())

def log(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return render(request, 'logsuccess.html',locals())
#				return HttpResponseRedirect("/logsuccess/")
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
	return render(request, 'logsuccess.html',locals())




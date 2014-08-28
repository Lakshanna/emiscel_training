from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from p4app.models import *
from p4app.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View

def home(request):
	return render(request, 'login.html',locals())

# def welcome(request):
# 	name= request.session['name']
# 	rk = StudentForm()
# 	return render(request,'welcome.html',locals())


	
# def signup(request):
# 	if request.method == 'POST':
# 		UF= UserForm
# 		UFr= UserForm(data = request.POST)
# 		UPr=UserProfileForm(data = request.POST)

# 		if UFr.is_valid() and UPr.is_valid():
# 			F = UFr.save()
# 			F.set_password(user.set_password)
# 			F.save()
# 			P = UPr.save(commit = False)
# 			P.user = user
# 			P.save()
# 			return HttpResponse('Your Profile Created Successfully')



def userform(request):
	test = UserForm()
	test1 = UserProfileForm()
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.set_password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
	return render(request, 'login.html', {'testht':test,'testht1':test1})	

def log(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				request.session['name']= username
				return HttpResponseRedirect('/welcome')
				
			else:
				return HttpResponse('Your Account is Disabled.')
		else:
			return HttpResponse('Invalid login details supplied.')
	return render(request, 'login.html', locals()	)

@login_required
def user_logout(request):
		logout(request)
		return HttpResponseRedirect('/')
# Create your views here.


@login_required
def welcome(request):
		name= request.session['name']
		return render(request,'welcome.html',locals())
		

class myentry(View):
	
	# @login_required
	def get(self,request,**kwargs):
		# name= request.session['name']
		form = StudentForm()
		return render(request,'entry.html',{'rk':form})

	# @login_required
	def post(self, request,**kwargs):
		# name= request.session['name']
		form = StudentForm(request.POST)
		if form.is_valid():
			if request.POST:
				s = Student(sid = request.POST['sid'],
				name = form.cleaned_data['name'],
				father_name= form.cleaned_data['father_name'],
				school = form.cleaned_data['school'],
				std= form.cleaned_data['std'],
				tamil = form.cleaned_data['tamil'],
				english = form.cleaned_data['english'],
				maths = form.cleaned_data['maths'],
				science = form.cleaned_data['science'],
				social = form.cleaned_data['social'],
				total = form.cleaned_data['total'],
				)
				s.save()
			marklist= Student.objects.all().order_by('sid')
			return render(request,'view.html',{'marklist':marklist})


# @login_required
class edit(View):
	# name= request.session['name']
	def get(self,request,**kwargs):
		pk = self.kwargs.get('pk')
		instance = Student.objects.get(sid = pk)
		return render(request,'edit.html',{'markdetails':instance,'pk1':pk})

	def post(self, request,**kwargs):
		pk = self.kwargs.get('pk')
		form = StudentForm(request.POST)
		if form.is_valid():
			sd= Student.objects.get(sid = pk)
			sd.sid = form.cleaned_data['sid']
			sd.name = form.cleaned_data['name']
			sd.father_name= form.cleaned_data['father_name']
			sd.school = form.cleaned_data['school']
			sd.std= form.cleaned_data['std']
			sd.tamil = form.cleaned_data['tamil']
			sd.english = form.cleaned_data['english']
			sd.maths = form.cleaned_data['maths']
			sd.science = form.cleaned_data['science']
			sd.social = form.cleaned_data['social']
			sd.total = form.cleaned_data['total']
			sd.save()
		else:
			return render(request,'edit.html',locals())

		marklist= Student.objects.get(sid = pk)
		return render(request,'view.html',{'marklist':marklist, 'pk':pk})


# @login_required
class view(View):
	# name= request.session['name']
	def get(self,request,**kwargs):
		marklist = Student.objects.all()
		return render(request,'view.html',{'marklist':marklist},)

	def post(self, request, **kwargs):
		marklist = Student.objects.all()
		return render(request,'view.html',{'marklist':marklist},)


# @login_required
class delete(View):
	# name= request.session['name']
	def get(self,request,**kwargs):
		pk = self.kwargs.get('pk')
		instance = Student.objects.get(sid = pk)
		return render(request,'delete.html',{'instance':instance, 'pk1':pk},)

	def post(self, request, **kwargs):
		pk = self.kwargs.get('pk')
		erase = Student.objects.get(sid = pk)
		erase.delete()
		return HttpResponseRedirect('/view/')


from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from sivaapp.models import *
from sivaapp.forms import  SignupForm,UserForm,StudentForm
from django.views.generic import View
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required



def loginauth(request):
	
	#request.session.set_test_cookie()
	if request.method=='POST':
		# import ipdb
		# ipdb.set_trace()
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user:
			if user.is_active:
				auth_login(request, user)
				request.session['username']=username
				print username
				a="You Have Logged in Successfully"
				return render(request,'home.html',locals())
			else:
				a="Your Account is disabled"
				return render(request,'home.html',locals())
		else:
			a='Invalid Login Details'
			return render(request,'home.html',locals())

	return render(request,'index.html',locals())

def home(request):
	#username=request.session['username']
	return render(request,'home.html',locals())

@login_required
def loginout(request):
	logout(request)	
	return render(request,'index.html',locals())


def signup(request):
	# import ipdb
	# ipdb.set_trace()
	if request.method=='POST':
		user_form=UserForm(data=request.POST)
		signup_form=SignupForm(data=request.POST)

		if user_form.is_valid() and signup_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			profile=signup_form.save(commit=False)
			profile.user=user
			profile.save()
			a='You Have Signed Up Successfully'
			return HttpResponseRedirect("/home")
	else:
		user_form = UserForm()
		profile_form = SignupForm()



	#mode=ContactForm()
	return render(request,'signup.html',locals())


class UserView(View):

	def get(self,request):
		username=request.session['username']
		mode=StudentForm()

		return render(request,'add.html',{'mode':mode})

	def post(self,request):
		# 
		#a=Contact(
		if request.POST:
			#import ipdb;ipdb.set_trace()
			first_name=request.POST['first_name']
			last_name=request.POST['last_name'] 
			email_id=request.POST['email_id']
			try:
				hostler=request.POST['hostler']
			except Exception:
				hostler=False

			sex=request.POST['sex']
			date=request.POST['date']
			photo_img=request.FILES['photo_img']
			classes=request.POST['classes']
			english=request.POST['english']
			tamil=request.POST['tamil']
			maths=request.POST['maths']
			science=request.POST['science']
			social=request.POST['social']
			a=Student(first_name=first_name,last_name=last_name,
				email_id=email_id,hostler=hostler,sex=sex,
				date=date,photo_img=photo_img,classes_id=classes,english=english,tamil=tamil,
				maths=maths,science=science,social=social)

			a.save()

			mode=StudentForm()
	
		return render(request,'add.html',locals())

@login_required
def  list(request):
	username=request.session['username']
	b=Student.objects.all()
	return render(request,'list.html',locals())



class UpdateView(View):
	def get(self,request,**kwargs):
		username=request.session['username']
		pk = self.kwargs.get('pk')
		instance = Student.objects.get(id=pk)
		return render(request,'edit.html',{'form_details':instance,'pk1':pk})

	def post(self,request,**kwargs):
		pk=self.kwargs.get('pk')
		form = StudentForm(request.POST)
		if form.is_valid():
			student_data = Student.objects.get(id=pk)
			student_data.first_name = form.cleaned_data['first_name']
			student_data.last_name= form.cleaned_data['last_name']
			student_data.email_id = form.cleaned_data['email_id']
			try:
				student_data.hostler=form.cleaned_data['hostler']
			except Exception:
				student_data.hostler=False
			student_data.date = form.cleaned_data['date']
			student_data.photo_img = form.cleaned_data['photo_img']
			student_data.classes = form.cleaned_data['classes']
			student_data.english = form.cleaned_data['english']
			student_data.tamil = form.cleaned_data['tamil']
			student_data.maths = form.cleaned_data['maths']
			student_data.tamil = form.cleaned_data['tamil']
			student_data.science = form.cleaned_data['science']
			student_data.social = form.cleaned_data['social']
			student_data.save()
			student_list = Student.objects.get(id=pk)
		return render(request,'edit.html',{'student_list':student_list, 'pk':pk})



class new_delete(View):
  	def get(self,request,**kwargs):
  		sid=kwargs.get("pk")
  		a=Student.objects.get(id=sid)
  		return render(request,"delete.html",locals())
  		

  	def post(self,request,**kwargs):
 	  	sid=kwargs.get("pk")
 	  	a=Student.objects.get(id=sid)
 	  	a.delete()
 	  	return HttpResponseRedirect('/list')
	
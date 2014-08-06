from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from studentapp.forms import *
from studentapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def signup(request):
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
			return HttpResponseRedirect("/home1")
	else:
		a=UserForm()
		b=UserProfileForm()
	return render(request,'signup.html',locals())
def home1(request):
	if request.POST:
		username = request.POST['txtuname']
		password = request.POST['txtpwd']
		request.session['uname']=username
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return render(request, 'base.html',locals())
			else:
				return HttpResponse("Your Account is disabled")
		else:
			return HttpResponse("Invalid login details supplied")
	return render(request, 'title.html', locals())

class new_stu(View):
	def get(self,request,**kwargs):
		uname=request.session['uname']
		f=studentform()
		return render(request,"new_stu.html",locals())
	def post(self,request,**kwargs):
		uname=request.session['uname']
		f=studentform(request.POST,request.FILES)
		if f.is_valid():
			b=studenttable(
				studentid=f.cleaned_data['studentid'],
				studnetname=f.cleaned_data['studnetname'],
				fathername=f.cleaned_data['fathername'],
				schoolname=f.cleaned_data['schoolname'],
				classes=f.cleaned_data['classes'],
				computer=int(f.cleaned_data['computer']),
				physics=int(f.cleaned_data['physics']),
				chemistry=int(f.cleaned_data['chemistry']),
				maths=int(f.cleaned_data['maths']),
				total=int(f.cleaned_data['computer'])+int(f.cleaned_data['physics'])+int(f.cleaned_data['chemistry'])+int(f.cleaned_data['maths'])
				)
			b.save()
		s=studenttable.objects.all()
		return render(request,"new_stu.html",locals())
class edit_stu(View):
	def get(self,request,**kwargs):
		uname=request.session['uname']
		f=studentform(request.POST)
		id1=self.kwargs.get('pk')
		id2 = str(id1)
		a=studenttable.objects.get(studentid=id2)
		return render(request,"edittable.html",locals())
	def post(self,request,**kwargs):
		uname=request.session['uname']
		sid=self.kwargs.get('pk')
		f=studentform(request.POST,request.FILES)
		b=studenttable.objects.get(studentid=sid)
		b.studentid=request.POST['studentid']
		b.studnetname=request.POST['studnetname']
		b.fathername=request.POST['fathername']
		b.schoolname=request.POST['schoolname']
		b.classes_id=request.POST['classes']
		b.computer=request.POST['computer']
		b.physics=request.POST['physics']
		b.chemistry=request.POST['chemistry']
		b.maths=request.POST['maths']
		b.total=int(request.POST['computer'])+int(request.POST['physics'])+int(request.POST['chemistry'])+int(request.POST['maths'])
		b.save()
		i=studenttable.objects.all()
		return render(request,"viewtable.html",{'b':i,'uname':uname})	
		
def view_stu(request):
	uname=request.session['uname']
	b = studenttable.objects.all()
	return render(request,"viewtable.html",locals())

class del_stu(View):
	def get(self,request,**kwargs):
		uname=request.session['uname']
		pk=self.kwargs.get('pk')
		instance=studenttable.objects.get(studentid=pk)
		return render(request,'deletetable.html',{'a':instance,'pk':pk,'uname':uname})
	def post(self,request,**kwargs):
		uname=request.session['uname']
		pk=self.kwargs.get('pk')
		quest1=studenttable.objects.get(studentid=pk)
		quest1.delete()
		uname=request.session['uname']
		b = studenttable.objects.all()
		return render(request,'viewtable.html',{'b':b,'uname':uname})
@login_required
def logot(request):
	logout(request)
	return HttpResponseRedirect("/home1")

def chpwd(request):
	if request.method == 'POST':
		user_form = UserForm1(data=request.POST)
		# username=request.POST['username']
		# password = request.POST['password']
		if user_form.is_valid():
			user=user_form.save()
		#profile_form = UserProfileForm(data=request.POST)
#		if request.POST:
#		user = authenticate(username=username, password=password)
			user.set_password(password)
			user.save()
			# profile = profile_form.save(commit=False)
			# profile.user = user
			# profile.save()
			return render(request,"/home1",locals())
		else:
			a=UserForm1()
		#b=UserProfileForm()
	return render(request,'changepwd.html',locals())

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from emisapp.forms import *
from emisapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	if request.POST:
		username = request.POST['txtuname']
		password = request.POST['txtpwd']
		request.session['uname']=username
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return render(request, 'home.html',locals())
			else:
				return HttpResponse("Your Account is disabled")
		else:
			return HttpResponse("Invalid login details supplied")
	return render(request, 'title.html', locals())


def signup(request):
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		
		if user_form.is_valid(): 
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			return HttpResponseRedirect('successacc.html')
	else:
		a=UserForm()
	return render(request,'signup.html',locals())
@login_required
def logot(request):
	logout(request)
	return HttpResponseRedirect("/")

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
				sid=f.cleaned_data['sid'],
				sname=f.cleaned_data['sname'],
				sphoto=request.FILES['sphoto'],
				sdob=f.cleaned_data['sdob'],
				scomm=f.cleaned_data['scomm'],
				scommcert=f.cleaned_data['scommcert'],
				srel=f.cleaned_data['srel'],
				slan=f.cleaned_data['slan'],
				sphone=int(f.cleaned_data['sphone']),
				sdis=f.cleaned_data['sdis'],
				sdabled=f.cleaned_data['sdabled'],
				scaste=f.cleaned_data['scaste'],
				snation=f.cleaned_data['snation'],
				spin=int(f.cleaned_data['spin']),
				sbg=f.cleaned_data['sbg'],
				smother=f.cleaned_data['smother'],
				smocc=f.cleaned_data['smocc'],
				smincome=int(f.cleaned_data['smincome']),
				sfather=f.cleaned_data['sfather'],
				sfocc=f.cleaned_data['sfocc'],
				sfincome=int(f.cleaned_data['sfincome']),
				sclass=f.cleaned_data['sclass'],
				ssection=f.cleaned_data['ssection'],
				smedium=f.cleaned_data['smedium'],
				sdistrict=f.cleaned_data['sdistrict'],
				sblock=f.cleaned_data['sblock'],
				sschool=f.cleaned_data['sschool'],
				sscode=int(f.cleaned_data['sscode']),
				sbank=f.cleaned_data['sbank'],
				saccno=int(f.cleaned_data['saccno']),
				ssports=f.cleaned_data['ssports'],
				ssname=f.cleaned_data['ssname'],
				aayear=f.cleaned_data['aayear']
				)
			b.save()
		s=studenttable.objects.all()
		return render(request,"new_stu.html",locals())
class edit_stu(View):
	def get(self,request,**kwargs):
		uname=request.session['uname']
		f=studentform(request.POST)
		i=studenttable.objects.filter(sclass=self.kwargs.get('pk'))
		return render(request,"viewtable.html",{'b':i})
class edit_stu2(View):
	def get(self,request,**kwargs):
		uname=request.session['uname']
		c=self.kwargs.get('pk')
		i=studenttable.objects.get(sid=c)
		return render(request,"viewall.html",locals())
class edit_stu1(View):
	def get(self,request,**kwargs):
		uname=request.session['uname']
		f=studentform(request.POST)
		id1=self.kwargs.get('pk')
		a=studenttable.objects.get(sid=id1)
		return render(request,"edittable.html",locals())
	def post(self,request,**kwargs):
		uname=request.session['uname']
		sid=self.kwargs.get('pk')
		f=studentform(request.POST,request.FILES)
		b=studenttable.objects.get(sid=sid)
		b.sid=request.POST['sid']
		b.sname=request.POST['sname']
		# b.sfather=request.POST['sfather']
		b.sschool=request.POST['sschool']
		b.sclass_id=request.POST['sclass']
		b.save()
		i=studenttable.objects.all()
		return render(request,"viewtable.html",{'b':i,'uname':uname})	
def view_stu(request):
	uname=request.session['uname']
	a1=studenttable.objects.filter(sclass='1').count()
	a2=studenttable.objects.filter(sclass='2').count()
	a3=studenttable.objects.filter(sclass='3').count()
	a4=studenttable.objects.filter(sclass='4').count()
	a5=studenttable.objects.filter(sclass='5').count()
	a6=studenttable.objects.filter(sclass='6').count()
	a7=studenttable.objects.filter(sclass='7').count()
	a8=studenttable.objects.filter(sclass='8').count()
	a9=studenttable.objects.filter(sclass='9').count()
	a10=studenttable.objects.filter(sclass='10').count()
	a11=studenttable.objects.filter(sclass='11').count()
	a12=studenttable.objects.filter(sclass='12').count()
	rec=studenttable.objects.all()
	total =rec.count()
	return render(request,"childelist.html",locals())
# class del_stu(View):
# 	def get(self,request,**kwargs):
# 		uname=request.session['uname']
# 		pk=self.kwargs.get('pk')
# 		instance=studenttable.objects.get(studentid=pk)
# 		return render(request,'deletetable.html',{'a':instance,'pk':pk,'uname':uname})
# 	def post(self,request,**kwargs):
# 		uname=request.session['uname']
# 		pk=self.kwargs.get('pk')
# 		quest1=studenttable.objects.get(studentid=pk)
# 		quest1.delete()
# 		uname=request.session['uname']
# 		b = studenttable.objects.all()
# 		return render(request,'viewtable.html',{'b':b,'uname':uname})

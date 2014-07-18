from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from helloapp.models import *
from helloapp.forms import *
import ipdb
# Create your views here.
def home(request):

	return render(request,"index.html",locals())

def new_stu(request):
	f=MyForm()
	if request.POST:
		roll_no=request.POST['roll_no']
		admin_dt=request.POST['admin_dt']
		first_name=request.POST['fname']
		last_name=request.POST['lname']
		# ipdb.set_trace()
		try:
			is_spl_stu=request.POST['is_spl_stu']
		except Exception:
			is_spl_stu=False

		photo=request.FILES['photo']
		email=request.POST['email']
		a= student(roll_no=roll_no,admin_dt=admin_dt,fname=first_name,lname=last_name,is_spl_stu=is_spl_stu,photo=photo,email=email)
		a.save()
		b = student.objects.all()
	return render(request,"new_stu.html",locals())



def edit(request):
	# if get_details button clicked
	if request.POST.get('get_details'):
		
		ID=request.POST['roll_no1']
		a=student.objects.get(roll_no = ID)

	#if save button clicked		
	if request.POST.get('save'):
		
		
		roll_no=request.POST.get('roll_no')
		admin_dt=request.POST.get('admin_dt')
		first_name=request.POST.get('fname')
		last_name=request.POST.get('lname')
		
		try:
			is_spl_stu=request.POST['is_spl_stu']
		except Exception:
			is_spl_stu=False
		photo=request.POST.get('photo')
		email=request.POST.get('email')
		b= student(roll_no=roll_no,admin_dt=admin_dt,fname=first_name,lname=last_name,is_spl_stu=is_spl_stu,photo=photo,email=email)
		b.save()
		return HttpResponseRedirect('/edit')
	
	# if delete button clicked	
	if request.POST.get('delete'):
		ID=request.POST.get('roll_no')
		a=student.objects.get(roll_no= ID)
		a.delete()
		return HttpResponseRedirect('/edit')
	return render(request,'edit.html',locals())

def view(request):
	b = student.objects.all()
	return render(request,"view.html",locals())

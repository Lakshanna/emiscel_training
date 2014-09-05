from django.shortcuts import render
from dbconvertapp.forms import *
from dbconvertapp.models import *
from django.views.generic import View
from django.http import HttpResponseRedirect
# Create your views here.
def entry(request):
       return render(request,"home.html",locals())   
class home1(View):
    def get(self,request,**kwargs):  
        return render(request, 'home.html', locals())
    def post(self,request,**kwargs):   
        if request.POST:
            username = request.POST['txtuname']
            request.session['blockname']=username
            password = request.POST['txtpwd']
            blockrec=Blocktable.objects.get(Block_Name=username)#, Block=password)
            print blockrec.Block
            print password
            if int(blockrec.Block)==int(password):
                schoolrec=Schoollist.objects.filter(Blockname=username)
                dschoolrec=Schoollist.objects.filter(Blockname=username).distinct('Districtname')
            else:
                return HttpResponseRedirect('/')                

        return render(request, 'edittable.html', locals())

class showdetails(View):
    def get(self,request,**kwargs):  
        return HttpResponseRedirect('/')
    def post(self,request,**kwargs):
            c=request.POST['udisecode']
            request.session['district']=request.POST['districtname']
            request.session['udisecode']=c
            schoolrec=Schoollist.objects.get(UDISEcode=c)
            return render(request,"schools.html",locals())
class calc1(View):
    def get(self,request,**kwargs):  
        return HttpResponseRedirect('/')
    def post(self,request,**kwargs):
        c=request.POST['btoi']
        #import ipdb; ipdb.set_trace()
        # blockname=request.session['blockname']
        udisecode=request.session['udisecode']
        district=request.session['district']
        b=Schoollist.objects.get(UDISEcode=udisecode)
        b.Districtname=request.POST['schoolname2']#request.session['district']
        b.Blockname=request.POST['blockname2']#request.session['blockname']
        b.UDISEcode=request.POST['schoolname1']#udisecode
        b.Schoolname=request.POST['schoolname']
        b.Management=request.POST['mgntname']
        b.Category=request.POST['cater']
        b.Girlsstrength=request.POST['gstr']
        b.Boysstrength=request.POST['bstr']
        b.Girlstoilet=request.POST['gtoi']
        b.Boystoilet=request.POST['btoi']
        b.Girlsworking=request.POST['gwork']
        b.Boysworking=request.POST['bwork']
        b.save()    
        schoolrec=Schoollist.objects.get(UDISEcode=udisecode)
        return render(request,"readdata.html",locals())
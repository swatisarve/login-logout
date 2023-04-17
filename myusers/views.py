from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Myusers 
from django.http import HttpResponseRedirect,HttpResponse
from myusers.models import Result
from django.template import loader
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        form=Myusers(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created.You can log in now!')
            return redirect('login')
    else:
        form=Myusers()
    context={
        'form':form
        }
    return render(request,'register.html',context)   

# def add(request):
#     if request.method=='POST':
#         firstname=request.POST.get('firstname')
#         lastname=request.POST.get('lastname')
#         emailid=request.POST.get('emailid')
#         mobilenumber=request.POST.get('mobilenumber')
#         gender=request.POST.get('gender')
#         result=Result(firstname=firstname, lastname=lastname,emailid=emailid, mobilenumber=mobilenumber, gender=gender)
#         result.save()
#     return render(request,'home.html')    

# def show(request):
#     data=Result.objects.all().values()
#     template=loader.get_template('home.html')
#     content={
#         'data':data
#     }
#     return HttpResponse(template.render(content,request))



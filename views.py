from django.contrib import messages

from django.http import HttpResponse
from django.shortcuts import redirect, render

from my_app.models import signup

# Create your views here.
# def home(request):
#     return HttpResponse("Hello world!")
def home(request):
    return render(request,"home.html")

def signin(request):
    return render(request,"signup.html")

def usertable(request):
    result=signup.objects.all()
    return render(request, "new.html",{'data':result})

def signup_submit(request):
    if request.method=="POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        email=request.POST.get("email")
        gender=request.POST.get("gender")
        t= signup(name=name,email=email,password=password,gender=gender)
        t.save()
        messages.success(request,"register successfull") 
        return redirect('usertable')
    
def update_view(request):
    return render(request,"update.html")

def update_submit(request,id):
    res=signup.objects.get(id=id)
    return render(request,"update.html",{'data':res})

def update_submit_data(request,id):
    if request.method=="POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        email=request.POST.get("email")
        gender=request.POST.get("gender") 
        s=signup.objects.get(id=id)        
        s.name=name
        s.email=email
        s.password=password
        s.gender=gender
        s.save()
        messages.success(request,"update data successfull")
        return redirect('usertable')


def delete_data(request,id):
    result=signup.objects.get(id=id)
    result.delete()
    messages.success(request,"delete data successfull")
    return redirect('usertable') 

def search_bar(request):
    return render(request,"search.html")

def search_data(request):
    query=request.POST.get('name','')
    r=[]
    if query:
        r=signup.objects.filter(name__icontains=query)
    return render(request,"search.html",{'query':query,'result':r})


    
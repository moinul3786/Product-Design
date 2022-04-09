


from django.shortcuts import render,HttpResponse,redirect
from h_apps.models import Contact
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,'home.html')
def index1(request):
    return render(request,'index1.html')
def logout(request):
    auth.logout(request)
    return redirect('login')
def about(request):
    return render(request,'about.html')
def register(request):
    if request.method == "POST":
        fname= request.POST['fname']
        lname= request.POST['lname']
        username= request.POST['username']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        email= request.POST['email']
       
       
        
        if pass1==pass2:
          if User.objects.filter(username=username).exists():
              messages.error(request,"Username already taken")
          if User.objects.filter(email=email).exists():
              messages.error(request,"email already taken")
          else:
              user = User.objects.create(username=username,first_name=fname,last_name=lname,email=email,password=pass1)
              user.save()
              if user is not None:
                  auth.login(request,user)
                  return render(request,'index1.html')
        else:
            messages.error(request,"Both Password are not matching")

    else:
      return render(request,'register.html')

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        Password=request.POST['password']
        user=auth.authenticate(username=username,password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect('index1')
        else:
            messages.error(request,"worng credentials")
            return render(request,'login.html')

    else:
         return render (request, 'login.html')

def contact(request):
    if request.method =='POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        country = request.POST.get('country')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.subject = subject
        contact.country= country
        contact.save()
       
        return HttpResponse(" Thanks ")

    return render (request, 'contact.html')
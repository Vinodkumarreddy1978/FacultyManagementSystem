from django.shortcuts import render,redirect
from .forms import facultyform
from student.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

def home(request):
    is_authenticated = request.user.is_authenticated
    return render(request, 'home.html', {'is_authenticated': is_authenticated})
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if not User.objects.filter(username=username):
            User.objects.create_user(username=username,email=email,password=password)
            return redirect('/login')
        else:
            messages.error(request,'user already exists')
    return render(request,'signup.html')
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid login credentials")
    return render(request,'login.html')
def signout(request):
    logout(request)
    return redirect('home')
@login_required()
def register(request):
    form=facultyform()
    if request.method=='POST':
        form=facultyform(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'register.html',{'form':form})
@login_required()
def view(request):
    st=faculty.objects.all()
    return render(request,'view.html',{'st':st})

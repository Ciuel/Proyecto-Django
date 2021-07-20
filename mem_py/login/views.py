from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import RegisterForm,LoginForm

# Create your views here.

def loginPage(request):
    form=LoginForm(request.POST or None)
    print(form.errors)
    if form.is_valid(): 
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user= authenticate(request,username=username,password=password)
        if user:
            login(request, user)
            return redirect('')

    return render(request,'login/login.html',{"form":form})


def registerPage(request):
    register=RegisterForm(request.POST or None)
    if register.is_valid():
        register.save()
        return redirect('login:login')
    return render(request,'login/register.html',{"form_register":register})
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

@login_required(login_url='login:login')
def menuPage(request):
    return render(request,'menu/menu.html',{})

@login_required(login_url='login:login')
def logoutPage(request):
    logout(request)
    return redirect('login:login')

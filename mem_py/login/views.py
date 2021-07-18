from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from .models import User

# Create your views here.

def login(request):
    login_form=LoginForm(request.POST or None)
    if login_form.is_valid():
        info=login_form.cleaned_data
        try:
            user=User.objects.get(nick=info["nickname"],password=info["password"])
            #HttpResponseRedirect('') Redireccion a la pagina inicial
        except:
            return render(request,'login/login.html',{"form_login":login_form,"usernotfound":True})
        
    return render(request,'login/login.html',{"form_login":login_form,"usernotfound":False})

def register(request):
    return render(request,'login/register.html',{
        "form_register":0
    })
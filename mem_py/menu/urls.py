from django.urls import path
from . import views

app_name='menu'
urlpatterns = [
    path("",views.menuPage,name='menu'),
    path("logout",views.logoutPage,name='logout')
]
from django import forms

# Create your forms here 

class LoginForm(forms.Form):
    nickname=forms.CharField(label="",max_length=25,widget=forms.TextInput(attrs={
        "placeholder":"Nickname",
        "id":"login_nick"
    }))
    password=forms.CharField(label="",max_length=16,widget=forms.PasswordInput(attrs={
        "placeholder":"Cotraseña",
        "id":"login_password"
    }))

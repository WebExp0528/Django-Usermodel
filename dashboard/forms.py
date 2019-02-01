from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=40)
    password = forms.CharField(label="Password", max_length=50)
    

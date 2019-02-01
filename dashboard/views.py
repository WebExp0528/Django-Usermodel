from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import View

from .models import User

class Authentication(View):
    # def loggedin(self):
    #     if 'username' in self.request.session:
    #         username = self.request.session['username']
    #     if 'email' in self.request.session:
    #         email = self.request.session['email']
    #     if 'token' in self.request.session:
    #         token = self.request.session['token']
    #     temp = json.decode(token)
    #     if temp.username == username and temp.email == email:
    #         return redirect('home')
    #     else:
    #         return redirect('login')

    def login(self):
        user_list = User.objects.all()
        context = {
            'user_list': user_list,
            'title': "Login"
        }
        return render(self, 'dashboard/auth/login.html', context)

    def auth(self):
        username = self.POST['username']
        password = self.POST['password']
        try:
            user = User.objects.filter(username=username, password=password)
        except User.DoesNotExist:
            user = []
        if len(user) > 0:
            # email = user[0].email
            # token = jwt.encode({'username': username, 'email': email}, 'SECRET', algorithm='HS256')
            # self.request.session['token'] = token
            # self.request.session['username'] = username
            # self.request.session['email'] = email
            return redirect('home')
        else:
            return redirect('login')

    def forgot(self):
        return render(self, 'dashboard/auth/forgot.html', {'title': 'Forgot Password'})

    def signup(self):
        return render(self, 'dashboard/auth/signup.html', {'title': 'Signup'})

    def register(self):
        username = self.POST['username']
        email = self.POST['email']
        password = self.POST['password']
        try:
            user = User.objects.filter(username=username, email=email)
        except User.DoesNotExist:
            user = []
        if len(user) > 0:
            return redirect('signup')
        else:
            new_admin = User(username=username, password=password, email=email)
            new_admin.save()
            return redirect('login')

    def reset_password(self):
        return redirect('forgot')

class Dashboard:
    # @Authentication.loggedin
    def home(self):
        return render(self, 'dashboard/main/home.html', {'title': 'Dashboard'})
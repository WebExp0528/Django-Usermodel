from django.urls import path
from django.views.generic import ListView
from .views import Authentication, Dashboard
from .models import User

urlpatterns = [
    path('login', Authentication.login, name='login'),
    path('auth', Authentication.auth, name='auth'),
    path('forgot', Authentication.forgot, name='forgot'),
    path('signup', Authentication.signup, name='signup'),
    path('register', Authentication.register, name='register'),
    path('reset', Authentication.reset_password, name='reset_password'),
    path('home', Dashboard.home, name='home')
]

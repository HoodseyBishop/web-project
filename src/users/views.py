from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


def user_list(request):
    return HttpResponse('All users here')


def user_detail(request, username):
    return HttpResponse('This is {}, and he/she is user'.format(username))


def user_signup(request):
    return HttpResponse('Sign Up here')


class Login(LoginView):
    template_name = 'users/user_login.html'


class Logout(LogoutView):
    template_name = 'users/user_logout.html'


def user_logout(request):
    return HttpResponse('Sign Up here')

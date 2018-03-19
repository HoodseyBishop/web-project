from django.shortcuts import render, HttpResponse

# Create your views here.


def user_list(request):
    return HttpResponse('All users here')


def user_detail(request, username):
    return HttpResponse('This is {}, and he/she is user'.format(username))


def user_signup(request):
    return HttpResponse('Sign Up here')


def user_login(request):
    return HttpResponse('Log In here')
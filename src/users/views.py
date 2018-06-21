from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from core.models import User
from .forms import SignUpForm


def user_list(request):
    return HttpResponse('All users here')


def user_detail(request, username):
    return HttpResponse('This is {}, and he/she is user'.format(username))


# def user_signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             username = form.data.get('username')
#             password = form.data.get('password1')
#             user = User.objects.create(
#                 username=username,
#                 password=password,
#             )
#             user = authenticate(username=username, password=password)
#             user.save()
#             # login(request, user)
#             return redirect('user_login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/user_signup.html', {'form': form})


class UserList(ListView):
    model = User
    queryset = User.objects.all().order_by('username')
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserDetail(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user_'


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'users/user_signup.html'

    # def get_success_url(self):
    #     return render(self.request, 'core/main.html')


class Login(LoginView):
    template_name = 'users/user_login.html'

    def get_success_url(self):
        return reverse('main')


class Logout(LogoutView):
    template_name = 'users/user_logout.html'


class UserEdit(UpdateView):
    model = User
    template_name = 'users/user_edit.html'
    fields = 'username', 'password', 'email'

    def get_queryset(self):
        queryset = super(UserEdit, self).get_queryset()
        queryset = queryset.filter(username=self.request.user.username)
        print(queryset)
        return queryset

    def get_success_url(self):
        return reverse('question_detail', kwargs={'pk': self.object.pk})

from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.models import User
from market.models import Profile


class Login(LoginView):
    http_method_names = ['get', 'post']
    redirect_authenticated_user = True
    template_name = 'login.html'


class Logout(LogoutView):
    http_method_names = ['get']
    template_name = 'logout.html'

    def get(self, *args, **kwargs):
        super().get(*args, **kwargs)
        return redirect('item_list_url')


class Register(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/'

    def form_valid(self, form):
        obj = form.save()
        Profile.objects.create(
            user=obj
        )
        return super().form_valid(form)
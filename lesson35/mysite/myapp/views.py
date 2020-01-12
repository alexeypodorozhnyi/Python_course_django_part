from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

from .models import Article,Comment


# Create your views


class ArticleList(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            articles = Article.objects.filter(name__icontains=search_query)
        else:
            articles = Article.objects.all()
        return render(request, 'index.html', context={'articles': articles})


def article_detail(request, id):
    article = Article.objects.get(pk = id)
    return render(request, 'article.html', context={'article':  article})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Comment
from .forms import CommentForm


# Create your views


class ArticleList(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            articles = Article.objects.filter(name__icontains=search_query)
        else:
            articles = Article.objects.all()
        return render(request, 'index.html', context={'articles': articles})


class CommentCreateView(CreateView):
    form_class = CommentForm
    success_url = '/'
    template_name = 'comment_create.html'
    model = Comment

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.article=self.request.article
            obj.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('')


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    success_url = '/'
    fields = ['name', 'text']


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = '/'


class ArticleDetailView(DetailView):
    model = Article
    success_url = 'article_detail_url'
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({'comment_create_form': CommentForm})
        return context




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

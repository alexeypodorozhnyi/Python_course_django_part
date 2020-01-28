from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Note,Profile
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from .forms import NoteForm,UpdateNoteForm,ConfirmEmailForm
from django.contrib.auth.models import User
import uuid
def index_page(request):
    return render(request, 'index.html')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class UserLoginView(LoginView):
    success_url = 'index_url'


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            Profile.objects.create(
                user=user,
                email_token=uuid.uuid4()
            )
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse('index_url'))
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class PostsListView(ListView):
    template_name = 'notes_list.html'
    model = Note
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            return super().get_queryset().filter(user=self.request.user).filter(name__icontains=search_query)
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'note_create_form': NoteForm,
                        'note_update_form': UpdateNoteForm}
                       )
        return context


class NoteCreateView(CreateView):
    form_class = NoteForm
    success_url = '/notes'
    template_name = 'note_create.html'
    model = Note

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_delete.html'
    success_url = '/notes'


class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'note_update.html'
    success_url = '/notes'
    fields = ['is_shared']


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'user_detail.html'
    success_url = 'profile_detail/'


class EmailUpdateView(UpdateView):
    model = Profile
    template_name = 'email_confirm.html'
    form_class = ConfirmEmailForm
    success_url = 'email_confirm_view/'

    def form_valid(self, form):
        obj = form.save(commit =False)
        return super().form_valid(form)


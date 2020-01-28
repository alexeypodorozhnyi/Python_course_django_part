from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView
from .views import user_register, PostsListView, UserLoginView, index_page,NoteCreateView,NoteDeleteView,NoteUpdateView,ProfileDetailView,EmailUpdateView

urlpatterns = [
    path('', index_page, name='first_url'),
    path('notes/', PostsListView.as_view(), name='index_url'),
    path('login/', UserLoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('register/', user_register, name='user_register_url'),
    path('note_create/',NoteCreateView.as_view(),name='note_create_url'),
    path('note_delete/<int:pk>', NoteDeleteView.as_view(), name='note_delete_url'),
    path('note_update/<int:pk>', NoteUpdateView.as_view(), name='note_update_url'),
    path('profile_detail/<int:pk>/',ProfileDetailView.as_view(),name='profile_detail_url'),
    path('email_confirm_view/<int:pk>/', EmailUpdateView.as_view(),name='email_confirm_url'),
]

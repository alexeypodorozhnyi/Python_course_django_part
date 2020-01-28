from django.contrib import admin
from django.urls import path

from .views import ArticleList, LogoutView, user_register, CommentCreateView, ArticleUpdateView, \
    ArticleDeleteView, ArticleDetailView
from django.contrib.auth.views import LoginView, PasswordChangeView

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list_url'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('register/', user_register, name='user_register_url'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change_url'),
    path('comment_create/', CommentCreateView.as_view(), name='comment_create_url'),
    path('article_update/<int:pk>', ArticleUpdateView.as_view(), name='article_update_view'),
    path('article_delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete_view'),
    path('article_detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail_url'),
]

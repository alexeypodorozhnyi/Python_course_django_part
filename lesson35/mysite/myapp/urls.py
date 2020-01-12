from django.contrib import admin
from django.urls import path

from .views import ArticleList,LogoutView,user_register,article_detail
from django.contrib.auth.views import LoginView,PasswordChangeView


urlpatterns = [
    path('', ArticleList.as_view(),name='article_list_url'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('register/',user_register,name='user_register_url'),
    path('password_change/',PasswordChangeView.as_view(),name='password_change_url'),
    path('article/<int:id>/',article_detail,name='article_detail_url')

]
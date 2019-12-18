from django.urls import path,re_path

from .views import new,edit,lock,processing,return_code

urlpatterns = [
    path('news/new', new, name='news-new'),
    path('news/edit', edit, name='news-edit'),
    path('news/lock', lock, name='news-lock'),
    path('news/<str:mode>/<int:item_id>',processing,name='articles-add'),
    re_path('news/'r'(?P<code>[0-9]{1}-[A-Za-z]{3}-[0-9]$)',return_code,name='news-code')
]
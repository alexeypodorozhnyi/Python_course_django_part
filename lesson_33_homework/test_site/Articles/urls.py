from django.urls import path,re_path

from .views import new,edit,lock,processing,return_code

urlpatterns = [
    path('articles/new', new, name='articles-new'),
    path('articles/edit', edit, name='articles-edit'),
    path('articles/lock', lock, name='articles-lock'),
    path('articles/<str:mode>/<int:item_id>',processing,name='articles-add'),
    re_path('articles/'r'(?P<code>[0-9]{2}[A-Za-z]{3}$)',return_code,name='articles-code')
]
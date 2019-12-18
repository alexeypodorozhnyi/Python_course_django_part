from django.urls import path,re_path

from .views import new,edit,lock,processing,phone_check

urlpatterns = [
    path('comments/new', new, name='comments-new'),
    path('comments/edit', edit, name='comments-edit'),
    path('comments/lock', lock, name='comments-lock'),
    path('comments/<str:mode>/<int:item_id>',processing,name='articles-add'),
    re_path('comments/user/phone/'r'(?P<phone>0(3|5|6||7|9)[0-9]-\d{3}-\d{2}-\d{2}$)',phone_check,name='phone')
]
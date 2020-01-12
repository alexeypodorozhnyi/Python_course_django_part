from django.urls import path

from .views import *
urlpatterns = [
    path('', AnimalList, name='index'),

]



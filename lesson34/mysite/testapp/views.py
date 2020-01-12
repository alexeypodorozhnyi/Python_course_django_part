from django.shortcuts import render
from django.views.generic import ListView
from .models import Animal


# Create your views

def AnimalList(request):
    animal = Animal.objects.all()
    return render(request,'animal_list.html',context={'animals' : animal})



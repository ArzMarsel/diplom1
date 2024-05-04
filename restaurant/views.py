from django.shortcuts import render
from django.views.generic import ListView
from .models import Dish


class List_of_dishes(ListView):
    model = Dish
    template_name = 'restaurant/main.html'
    context_object_name = 'dish'



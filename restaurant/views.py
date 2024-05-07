from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Dish, Dish_image


class List_of_dishes(ListView):
    model = Dish
    template_name = 'restaurant/main.html'
    context_object_name = 'dish'


class DetailDish(DetailView):
    model = Dish_image
    template_name = 'restaurant/more_dish.html'
    context_object_name = 'dish'




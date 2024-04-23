from django.urls import path
from . import views

urlpatterns = [
    path('', views.List_of_dishes.as_view(), name='Dishes')
]
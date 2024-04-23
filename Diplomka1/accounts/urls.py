from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('reg/login/', LoginView.as_view(), name='login'),
    # path('reg/register/', )
]
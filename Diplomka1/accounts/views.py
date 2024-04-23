from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


class User_creation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


def register(request):
    if request.method == 'POST':
        form = User_creation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = User_creation()
    return render(request, 'register/registrate.html', {'form': form})
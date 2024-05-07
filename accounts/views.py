from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django_recaptcha.fields import ReCaptchaField
from .forms import UserCreation


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'register/login.html')


def register(request):
    captcha = ReCaptchaField()
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreation()
    return render(request, 'register/registrate.html', {'form': form, 'captcha': captcha})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.conf import settings

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            error = "Invalid username or password"
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'register.html', {'error': "Passwords do not match"})
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': "Username already exists"})
        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'register.html')
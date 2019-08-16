from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


@login_required(login_url="/erp/login")
def erp_home(request):
    return render(request, "home.html")


def login_user(request):
    return render(request, "login.html")


def auth(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('home'))
    else:
        return redirect(('login'))


def logout_user(request):
    logout(request)
    return redirect(('login'))

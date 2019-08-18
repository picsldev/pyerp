from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from ..base.models import PyPartner, PyProduct
from django.contrib.auth.models import User


@login_required(login_url="/erp/login")
def erp_home(request):
    partners = PyPartner.objects.all()
    return render(request, "home.html", {
        'customers': partners.filter(customer=True),
        'providers': partners.filter(provider=True),
        'users': User.objects.all(),
        'products': PyProduct.objects.all()
    })


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

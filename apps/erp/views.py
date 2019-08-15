from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import logout, login


@login_required(login_url="/erp/login")
def erp_home(request):
    return render(request, "home.html")

# Public
def login_user(request):
    return render(request, "login.html")


def auth(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/erp/')
    else:
        return redirect('/erp/login')
        
    # import pdb;pdb.set_trace()

def logout_user(request): 
    logout(request)
    return redirect('/erp/login')
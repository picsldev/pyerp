from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import logout, login

"""
@login_required(login_url="/erp/home")
def erp_home(request):
    return render(request, "home.html")"""

# Public
def login_user(request):
    return render(request, "login.html")
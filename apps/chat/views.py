# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


@login_required(login_url="/erp/login")
def chat_home(request):
    return render(request, "pychat.html")

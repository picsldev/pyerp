from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def shop(request):
    return render(request, 'shop.html')

def post(request):
    return render(request, 'post.html')

def license(request):
    return render(request, 'license.html')

from __future__ import unicode_literals
from ..website.submodels.post import PyPost
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def post(request):
    return render(request, 'post.html')

def license(request):
    return render(request, 'license.html')

"""
BLOG
"""

def blog(request):
    posts = PyPost.objects
    return render(request, 'blog.html', {'posts':posts})

def post(request, post_id):
    postdetail = get_object_or_404(PyPost, pk=post_id)
    return render(request, 'post.html', {'post':postdetail})

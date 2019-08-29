from django.conf.urls import url
from .views import chat_home
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    url(r'chat-home', chat_home, name='chat-home'),
]

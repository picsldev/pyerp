# Librerias Django
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

# Librerias en carpetas locales
from .subviews.trigger import (
    DeleteTrigger, TriggerCreateView, TriggerDetailView, TriggerListView,
    TriggersUpdateView)
from .views import chat_home

urlpatterns = [
    url(r'chat-home', chat_home, name='chat-home'),
    path('triggers', TriggerListView.as_view(), name='triggers'),
    path('trigger/add/', TriggerCreateView.as_view(), name='trigger-add'),
    path('trigger/<int:pk>/', TriggerDetailView.as_view(), name='trigger-detail'),
    path('trigger/<int:pk>/update', TriggersUpdateView.as_view(), name='trigger-update'),
    path('trigger/<int:pk>/delete/', DeleteTrigger, name='trigger-delete'),
]

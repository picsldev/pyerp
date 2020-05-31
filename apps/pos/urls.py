# Librerias Django
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url
from .views import PosIndex

# Librerias en carpetas locales
from .subviews.pos import (
    DeletePos, PosCreateView, PosDetailView, PosListView, PosUpdateView)

urlpatterns = [
    url('pos-index', PosIndex, name='pos-index'),
    path('pos', PosListView.as_view(), name='pos'),
    path('pos/add/', PosCreateView.as_view(), name='pos-add'),
    path('pos/<int:pk>/', PosDetailView.as_view(), name='pos-detail'),
    path('pos/<int:pk>/update', PosUpdateView.as_view(), name='pos-update'),
    path('pos/<int:pk>/delete/', DeletePos, name='pos-delete'),
]

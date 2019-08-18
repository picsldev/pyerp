from django.urls import path
from django.contrib.auth import views as auth_views
from ..pos.views import PosListView, PosDetailView, PosCreateView, PosUpdateView, DeletePos


urlpatterns = [
    path('pos', PosListView.as_view(), name='pos'),
    path('pos/add/', PosCreateView.as_view(), name='pos-add'),
    path('pos/<int:pk>/', PosDetailView.as_view(), name='pos-detail'),
    path('pos/<int:pk>/update', PosUpdateView.as_view(), name='pos-update'),
    path('pos/<int:pk>/delete/', DeletePos, name='pos-delete'),
]
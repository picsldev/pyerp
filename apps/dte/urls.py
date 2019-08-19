from django.urls import path
from django.contrib.auth import views as auth_views
from .subviews.economical_activitie import EconomicalActivitieListView, EconomicalActivitieDetailView, EconomicalActivitieCreateView, EconomicalActivitieUpdateView, DeleteEconomicalActivitie


urlpatterns = [
    path('economical-activitie', EconomicalActivitieListView.as_view(), name='economical-activitie'),
    path('economical-activitie/add/', EconomicalActivitieCreateView.as_view(), name='economical-activitie-add'),
    path('economical-activitie/<int:pk>/', EconomicalActivitieDetailView.as_view(), name='economical-activitie-detail'),
    path('economical-activitie/<int:pk>/update', EconomicalActivitieUpdateView.as_view(), name='economical-activitie-update'),
    path('economical-activitie/<int:pk>/delete/', DeleteEconomicalActivitie, name='economical-activitie-delete'),
]

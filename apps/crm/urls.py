from django.urls import path
from django.contrib.auth import views as auth_views
from ..crm.views import LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, DeleteLead


urlpatterns = [
    path('lead', LeadListView.as_view(), name='lead'),
    path('lead/add/', LeadCreateView.as_view(), name='lead-add'),
    path('lead/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('lead/<int:pk>/update', LeadUpdateView.as_view(), name='lead-update'),
    path('lead/<int:pk>/delete/', DeleteLead, name='lead-delete'),
]

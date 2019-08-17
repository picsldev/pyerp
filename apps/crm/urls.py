from django.urls import path
from django.contrib.auth import views as auth_views
from ..crm.views import LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, DeleteLead
from ..crm.views import StageListView, StageDetailView, StageCreateView, StageUpdateView, DeleteStage
from ..crm.views import DashboardCrmView


urlpatterns = [
    path('dashboard-crm', DashboardCrmView, name='dashboard-crm'),

    path('lead', LeadListView.as_view(), name='lead'),
    path('lead/add/', LeadCreateView.as_view(), name='lead-add'),
    path('lead/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('lead/<int:pk>/update', LeadUpdateView.as_view(), name='lead-update'),
    path('lead/<int:pk>/delete/', DeleteLead, name='lead-delete'),

    path('stage', StageListView.as_view(), name='stage'),
    path('stage/add/', StageCreateView.as_view(), name='stage-add'),
    path('stage/<int:pk>/', StageDetailView.as_view(), name='stage-detail'),
    path('stage/<int:pk>/update', StageUpdateView.as_view(), name='stage-update'),
    path('stage/<int:pk>/delete/', DeleteStage, name='stage-delete'),
]

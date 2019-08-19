from django.urls import path
from django.contrib.auth import views as auth_views
from .subviews.accountplan import AccountPlanListView, AccountPlanDetailView, AccountPlanCreateView, AccountPlanUpdateView, DeleteAccountPlan


urlpatterns = [
    path('accountplan', AccountPlanListView.as_view(), name='accountplan'),
    path('accountplan/add/', AccountPlanCreateView.as_view(), name='accountplan-add'),
    path('accountplan/<int:pk>/', AccountPlanDetailView.as_view(), name='accountplan-detail'),
    path('accountplan/<int:pk>/update', AccountPlanUpdateView.as_view(), name='accountplan-update'),
    path('accountplan/<int:pk>/delete/', DeleteAccountPlan, name='accountplan-delete'),
]
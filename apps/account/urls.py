from django.urls import path
from django.contrib.auth import views as auth_views
from .subviews.accountplan import AccountPlanListView, AccountPlanDetailView, AccountPlanCreateView, AccountPlanUpdateView, DeleteAccountPlan
from .subviews.accountmove import AccountMoveListView, AccountMoveDetailView, AccountMoveCreateView, AccountMoveUpdateView, DeleteAccountMove

urlpatterns = [
    path('accountplan', AccountPlanListView.as_view(), name='accountplan'),
    path('accountplan/add/', AccountPlanCreateView.as_view(), name='accountplan-add'),
    path('accountplan/<int:pk>/', AccountPlanDetailView.as_view(), name='accountplan-detail'),
    path('accountplan/<int:pk>/update', AccountPlanUpdateView.as_view(), name='accountplan-update'),
    path('accountplan/<int:pk>/delete/', DeleteAccountPlan, name='accountplan-delete'),

    path('accountmove', AccountMoveListView.as_view(), name='accountmove'),
    path('accountmove/add/', AccountMoveCreateView.as_view(), name='accountmove-add'),
    path('accountmove/<int:pk>/', AccountMoveDetailView.as_view(), name='accountmove-detail'),
    path('accountmove/<int:pk>/update', AccountMoveUpdateView.as_view(), name='accountmove-update'),
    path('accountmove/<int:pk>/delete/', DeleteAccountMove, name='accountmove-delete'),
]
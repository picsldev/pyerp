from django.urls import path
from django.contrib.auth import views as auth_views
from ..project.views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, DeleteTask


urlpatterns = [
    path('task', TaskListView.as_view(), name='task'),
    path('task/add/', TaskCreateView.as_view(), name='task-add'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', DeleteTask, name='task-delete'),
]
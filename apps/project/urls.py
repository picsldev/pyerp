from django.urls import path
from django.contrib.auth import views as auth_views
from .subviews.task import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, DeleteTask
from .subviews.project import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, DeleteProject
from .subviews.bug import BugListView, BugDetailView, BugCreateView, BugUpdateView, DeleteBug

urlpatterns = [
    path('task', TaskListView.as_view(), name='task'),
    path('task/add/', TaskCreateView.as_view(), name='task-add'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', DeleteTask, name='task-delete'),

    path('project', ProjectListView.as_view(), name='project'),
    path('project/add/', ProjectCreateView.as_view(), name='project-add'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', DeleteProject, name='project-delete'),

    path('bug', BugListView.as_view(), name='bug'),
    path('bug/add/', BugCreateView.as_view(), name='bug-add'),
    path('bug/<int:pk>/', BugDetailView.as_view(), name='bug-detail'),
    path('bug/<int:pk>/update', BugUpdateView.as_view(), name='bug-update'),
    path('bug/<int:pk>/delete/', DeleteBug, name='bug-delete'),
]
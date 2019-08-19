from django.urls import path
from django.contrib.auth import views as auth_views
from .subviews.employee import EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, DeleteEmployee
from .subviews.department import DepartmentListView, DepartmentDetailView, DepartmentCreateView, DepartmentUpdateView, DeleteDepartment

urlpatterns = [
    path('employee', EmployeeListView.as_view(), name='employee'),
    path('employee/add/', EmployeeCreateView.as_view(), name='employee-add'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/update', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', DeleteEmployee, name='employee-delete'),

    path('department', DepartmentListView.as_view(), name='department'),
    path('department/add/', DepartmentCreateView.as_view(), name='department-add'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('department/<int:pk>/update', DepartmentUpdateView.as_view(), name='department-update'),
    path('department/<int:pk>/delete/', DeleteDepartment, name='department-delete'),
]
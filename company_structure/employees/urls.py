from django.urls import path
from .views import (
    DepartmentListView,
    DepartmentDetailView,
    PositionListView,
    PositionDetailView,
    EmployeeListView,
    EmployeeDetailView,
    PermissionListView,
    PermissionDetailView,
)

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),

    path('positions/', PositionListView.as_view(), name='position-list-create'),
    path('positions/<int:pk>/', PositionDetailView.as_view(), name='position-detail'),

    path('employees/', EmployeeListView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),

    path('permissions/', PermissionListView.as_view(), name='permission-list-create'),
    path('permissions/<int:pk>/', PermissionDetailView.as_view(), name='permission-detail'),
]

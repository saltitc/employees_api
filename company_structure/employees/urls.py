from django.urls import path
from .views import DepartmentListCreateView, PositionListCreateView, EmployeeListCreateView, PermissionListCreateView

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('positions/', PositionListCreateView.as_view(), name='position-list-create'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('permissions/', PermissionListCreateView.as_view(), name='permission-list-create'),
]

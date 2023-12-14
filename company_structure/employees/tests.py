from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse_lazy
from .models import Department, Position, Employee, Permission


class DepartmentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.department = Department.objects.create(name='IT Department')

    def test_get_department_list(self):
        url = reverse_lazy('department-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'IT Department')

    def test_create_department(self):
        url = reverse_lazy('department-list-create')
        data = {'name': 'Finance Department'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 2)

    def test_get_department_detail(self):
        url = reverse_lazy('department-detail', kwargs={'pk': self.department.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'IT Department')

    def test_update_department(self):
        url = reverse_lazy('department-detail', kwargs={'pk': self.department.id})
        data = {'name': 'Updated IT Department'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.department.refresh_from_db()
        self.assertEqual(self.department.name, 'Updated IT Department')

    def test_delete_department(self):
        url = reverse_lazy('department-detail', kwargs={'pk': self.department.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Department.objects.count(), 0)


class PositionAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.position = Position.objects.create(name='Developer')

    def test_get_position_list(self):
        url = reverse_lazy('position-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Developer')

    def test_create_position(self):
        url = reverse_lazy('position-list-create')
        data = {'name': 'Tester'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Position.objects.count(), 2)

    def test_get_position_detail(self):
        url = reverse_lazy('position-detail', kwargs={'pk': self.position.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Developer')

    def test_update_position(self):
        url = reverse_lazy('position-detail', kwargs={'pk': self.position.id})
        data = {'name': 'Updated Developer'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.position.refresh_from_db()
        self.assertEqual(self.position.name, 'Updated Developer')

    def test_delete_position(self):
        url = reverse_lazy('position-detail', kwargs={'pk': self.position.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Position.objects.count(), 0)


class EmployeeAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.department = Department.objects.create(name='IT Department')
        self.position = Position.objects.create(name='Developer')
        self.employee = Employee.objects.create(name='Test User', department=self.department)
        self.employee.positions.add(self.position)

    def test_get_employee_list(self):
        url = reverse_lazy('employee-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test User')

    def test_create_employee(self):
        url = reverse_lazy('employee-list-create')
        data = {'name': 'Jane Smith', 'department': self.department.id, 'positions': [self.position.id]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)

    def test_get_employee_detail(self):
        url = reverse_lazy('employee-detail', kwargs={'pk': self.employee.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test User')

    def test_update_employee(self):
        url = reverse_lazy('employee-detail', kwargs={'pk': self.employee.id})
        data = {'name': 'Updated Test User'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.name, 'Updated Test User')

    def test_delete_employee(self):
        url = reverse_lazy('employee-detail', kwargs={'pk': self.employee.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)


class PermissionAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.position = Position.objects.create(name='Developer')
        self.permission = Permission.objects.create(position=self.position, name='Code Access')

    def test_get_permission_list(self):
        url = reverse_lazy('permission-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Code Access')

    def test_create_permission(self):
        url = reverse_lazy('permission-list-create')
        data = {'position': self.position.id, 'name': 'Read Access'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Permission.objects.count(), 2)

    def test_get_permission_detail(self):
        url = reverse_lazy('permission-detail', kwargs={'pk': self.permission.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Code Access')

    def test_update_permission(self):
        url = reverse_lazy('permission-detail', kwargs={'pk': self.permission.id})
        data = {'name': 'Updated Code Access'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.permission.refresh_from_db()
        self.assertEqual(self.permission.name, 'Updated Code Access')

    def test_delete_permission(self):
        url = reverse_lazy('permission-detail', kwargs={'pk': self.permission.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Permission.objects.count(), 0)

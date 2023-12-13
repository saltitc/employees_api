from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Department, Position, Employee, Permission


class EmployeeAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.department = Department.objects.create(name='IT Department')
        self.position = Position.objects.create(name='Developer')
        self.employee = Employee.objects.create(name='Test User', department=self.department)
        self.employee.positions.add(self.position)
        self.permission = Permission.objects.create(position=self.position, name='Code Access')

    def test_get_departments_list(self):
        response = self.client.get('/api/departments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'IT Department')

    def test_create_department(self):
        data = {'name': 'Finance Department'}
        response = self.client.post('/api/departments/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 2)

    def test_get_positions_list(self):
        response = self.client.get('/api/positions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Developer')

    def test_create_position(self):
        data = {'name': 'Tester'}
        response = self.client.post('/api/positions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Position.objects.count(), 2)

    def test_get_employees_list(self):
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test User')

    def test_create_employee(self):
        data = {'name': 'Jane Smith', 'department': self.department.id, 'positions': [self.position.id]}
        response = self.client.post('/api/employees/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)

    def test_get_permissions_list(self):
        response = self.client.get('/api/permissions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Code Access')

    def test_create_permission(self):
        data = {'position': self.position.id, 'name': 'Read Access'}
        response = self.client.post('/api/permissions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Permission.objects.count(), 2)

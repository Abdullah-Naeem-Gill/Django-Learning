from django.urls import path
from employees.views import Employees, EmployeeDetails

urlpatterns = [
    path('employees/', Employees.as_view(), name='employees'),
    path('employees/<uuid:pk>/', EmployeeDetails.as_view())
]

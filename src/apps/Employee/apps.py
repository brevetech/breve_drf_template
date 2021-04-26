from django.apps import AppConfig
# from src.apps.Employee.models import EmployeeModel


class UserConfig(AppConfig): 
    name = 'django.contrib.auth'
    verbose_name = 'Autenticación y autorización'


class EmployeeConfig(AppConfig):
    name = 'src.apps.Employee'
    verbose_name = 'Empleados'

from django.apps import AppConfig
# from breve_drf_template.apps.Employee.models import EmployeeModel


class UserConfig(AppConfig): 
    name = 'django.contrib.auth'
    verbose_name = 'Autenticación y autorización'


class EmployeeConfig(AppConfig):
    name = 'breve_drf_template.apps.Employee'
    verbose_name = 'Empleados'

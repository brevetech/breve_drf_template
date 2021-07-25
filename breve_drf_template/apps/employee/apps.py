from django.apps import AppConfig


# from breve_drf_template.apps.employee.models import EmployeeModel


class UserConfig(AppConfig):
    name = 'django.contrib.auth'
    verbose_name = 'Autenticación y autorización'


class EmployeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'breve_drf_template.apps.employee'
    verbose_name = 'Empleados'

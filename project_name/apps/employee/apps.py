from django.apps import AppConfig


class UserConfig(AppConfig):
    name = "django.contrib.auth"
    verbose_name = "Autenticación y autorización"


class EmployeeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "project_name.apps.employee"
    verbose_name = "Empleados"

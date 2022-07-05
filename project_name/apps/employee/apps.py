from django.apps import AppConfig


class UserConfig(AppConfig):
    """User app config"""

    name = "django.contrib.auth"
    verbose_name = "Autenticación y autorización"


class EmployeeConfig(AppConfig):
    """Employee app config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "project_name.apps.employee"
    verbose_name = "Empleados"

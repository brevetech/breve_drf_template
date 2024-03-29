from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Core app config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "{{project_name}}.apps.core"
    verbose_name = "core"

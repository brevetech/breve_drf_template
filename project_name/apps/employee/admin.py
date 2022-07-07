from django.contrib.admin import ModelAdmin, register

from project_name.apps.employee.models import EmployeeModel


@register(EmployeeModel)
class EmployeeAdmin(ModelAdmin):
    """Employee admin settings"""

    list_display = ("dni", "phone_number", "labor_specialty")

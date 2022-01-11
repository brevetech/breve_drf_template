from django.contrib.admin import register, ModelAdmin

from project_name.apps.employee.models import EmployeeModel


@register(EmployeeModel)
class EmployeeAdmin(ModelAdmin):
    list_display = ('dni', 'phone_number', 'labor_specialty')

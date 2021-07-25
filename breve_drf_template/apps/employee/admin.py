from django.contrib.admin import register, ModelAdmin

from breve_drf_template.apps.employee.models import EmployeeModel


@register(EmployeeModel)
class EmployeeAdmin(ModelAdmin):
    list_display = ('dni', 'phone_number', 'labor_specialty')

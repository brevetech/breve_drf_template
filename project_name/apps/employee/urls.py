from django.urls import path, include
from rest_framework import routers

from project_name.apps.employee.views import EmployeeView

router = routers.DefaultRouter()

router.register(r'employee', EmployeeView)

employee_urls = ([
                     path('', include(router.urls))
                 ], 'employee')

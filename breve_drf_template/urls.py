from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from breve_drf_template.apps.Employee.views import EmployeeView, EmployeeAuthenticatedView

router = routers.DefaultRouter()
# Employee pahts
router.register(r'employee', EmployeeView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/current_user', EmployeeAuthenticatedView.as_view())
]

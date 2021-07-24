from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers, permissions

from breve_drf_template.apps.core.urls import core_urls
from breve_drf_template.apps.employee.urls import employee_urls
from breve_drf_template.apps.employee.views import EmployeeView
from breve_drf_template.apps.core.views import LocationViewSet
from breve_drf_template.util import read_docs_md

router = routers.DefaultRouter()

# employee pahts
router.register(r'employee', EmployeeView)

urlpatterns = [
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    # set openapi docs as home
    path('', SpectacularRedocView.as_view(url_name='schema'), name='apidocs'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(core_urls)),
    path('api/v1/', include(employee_urls)),
]

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers, permissions

from breve_drf_template.apps.Employee.views import EmployeeView
from breve_drf_template.apps.core.views import LocationViewSet
from breve_drf_template.util import read_docs_md

router = routers.DefaultRouter()

# Employee pahts
router.register(r'employee', EmployeeView)
# Core paths
router.register(r'locations', LocationViewSet, basename='locations')

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # set openapi docs as home
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

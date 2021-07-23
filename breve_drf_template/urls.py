from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from drf_yasg import openapi
from drf_yasg.openapi import Contact
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from breve_drf_template.apps.Employee.views import EmployeeView
from breve_drf_template.apps.core.views import LocationViewSet
from breve_drf_template.util import read_docs_md

router = routers.DefaultRouter()
# swagger path
schema_view = get_schema_view(
    openapi.Info(
        title='Service Breve OpenAPI',
        default_version='v1.0',
        description=read_docs_md("index"),
        contact=Contact(
            name='Brevetech AS. (Team Mango 🥭)',
            email='teammango.dev@brevetech.com',
            url='https://brevetech.com')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    validators=['ssv', 'flex']
)

# Employee pahts
router.register(r'employee', EmployeeView)
# Core paths
router.register(r'locations', LocationViewSet, basename='locations')

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # set openapi docs as home
    path('', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

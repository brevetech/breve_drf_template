from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.openapi import Contact
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from breve_drf_template.apps.Employee.views import EmployeeView, EmployeeAuthenticatedView

router = routers.DefaultRouter()
# swagger path
schema_view = get_schema_view(
    openapi.Info(
        title='Service Breve OpenAPI',
        default_version='v1.0',
        description='# Hola a todos',
        contact=Contact(
            name='Brevetech AS. (Team Mango 🥭)',
            email='team_mango.dev@brevetech.com',
            url='https://brevetech.com')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    validators=['ssv', 'flex']
)

# Employee pahts
router.register(r'employee', EmployeeView)

urlpatterns = [
    # set openapi docs as home
    path('', schema_view.with_ui('swagger', cache_timeout = 0)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/current_user', EmployeeAuthenticatedView.as_view()),
]

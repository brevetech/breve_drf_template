"Project global URLS"

from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from {{project_name}}.apps.core.urls import core_urls
from {{project_name}}.apps.employee.urls import employee_urls

urlpatterns = [
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    # set openapi docs as home
    path("", SpectacularRedocView.as_view(url_name="schema"), name="apidocs"),
    path("admin/", admin.site.urls),
    path("api/v1/auth/", TokenObtainPairView.as_view(), name="auth_get_token"),
    path("api/v1/auth/refresh/", TokenRefreshView.as_view(), name="auth_refresh_token"),
    path("api/v1/", include(core_urls)),
    path("api/v1/", include(employee_urls)),
]

handler404 = "{{project_name}}.common.views.error_404"
handler500 = "{{project_name}}.common.views.error_500"

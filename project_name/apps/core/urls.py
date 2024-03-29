from django.urls import include, path
from rest_framework import routers
from {{project_name}}.apps.core.views import LocationViewSet

router = routers.DefaultRouter()

router.register("locations", LocationViewSet, basename="locations")

core_urls = ([path("", include(router.urls))], "core")

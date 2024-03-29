from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from {{project_name}}.apps.core.handlers.list_locations import list_locations
from {{project_name}}.apps.core.serializers import LocationSerializer
from {{project_name}}.common.serializers import ErrorSerializer
from {{project_name}}.common.utils import read_docs_md

# About Swagger method_decorator

# If you want to doc a default method of a Class Viewset,
# you have to put the method_decorator directly above of
# the viewset class code, and specify the name of the method
# that you want to doc. E.g. name='list' for the list
# method.

# If you want to doc an override Class Viewset method,
# or a View method, you have to place the method_decorator
# directly above of the desired method, without the name param


@method_decorator(
    name="list",
    decorator=extend_schema(
        summary="Location list",
        description=read_docs_md("endpoints/core/list"),
        responses={
            200: LocationSerializer(many=True),
            400: ErrorSerializer(),
            500: ErrorSerializer(),
        },
    ),
)
class LocationViewSet(viewsets.ViewSet):
    """
    Locations views
    """

    def list(self, request):
        """Gets a list of locations"""
        query = list_locations()
        serializer = LocationSerializer(query, many=True)
        return Response(serializer.data)

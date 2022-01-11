import logging

from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication

from project_name.common.serializers import ErrorSerializer
from project_name.apps.employee.models import EmployeeModel
from project_name.apps.employee.serializers import EmployeeSerializer
from project_name.paginators import DefaultPagination
from project_name.common.utils import read_docs_md

logger = logging.getLogger('watchtower-logger')

"""
About Swagger method_decorator

If you want to doc a default method of a Class Viewset, 
you have to put the method_decorator directly above of
the viewset class code, and specify the name of the method
that you want to doc. E.g. name='list' for the list
method.

If you want to doc an override Class Viewset method, 
or a View method, you have to place the method_decorator
directly above of the desired method, without the name param
"""


# remember use method_decorator for detailed documentation

@method_decorator(name='list', decorator=extend_schema(
    description=read_docs_md('endpoints/employee/list'),
    responses={
        200: EmployeeSerializer(many=True),
        400: ErrorSerializer()
    }
))
@method_decorator(name='retrieve', decorator=extend_schema(
    description=read_docs_md('endpoints/employee/retrieve'),
    responses={
        200: EmployeeSerializer(many=False),
        400: ErrorSerializer()
    }
))
class EmployeeView(viewsets.ModelViewSet):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    queryset = EmployeeModel.objects.filter(user__is_active=True)
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__last_name', 'user__email', 'dni']
    http_method_names = ['get']
    pagination_class = DefaultPagination

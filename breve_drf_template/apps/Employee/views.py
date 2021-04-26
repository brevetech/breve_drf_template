import logging

from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView

from breve_drf_template.apps.Common.Errors.serializer import ErrorSerializer
from breve_drf_template.apps.Employee.models import EmployeeModel
from breve_drf_template.apps.Employee.serializers import EmployeeSerializer
from breve_drf_template.paginators import DefaultPagination

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

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description='# Get Employee List\n'
                          'Get employees listed and optionally filtered',
    responses={
        200: EmployeeSerializer(many=True),
        400: ErrorSerializer()
    }
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description='# Get Employee by ID\n'
                          'Get employee data by its ID',
    responses={
        200: EmployeeSerializer(many=False),
        400: ErrorSerializer()
    }
))
class EmployeeView(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.filter(user__is_active=True)
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__last_name', 'user__email', 'dni']
    http_method_names = ['get']
    pagination_class = DefaultPagination


class EmployeeAuthenticatedView(APIView):

    @method_decorator(decorator=swagger_auto_schema(
        operation_description='# Get Current User Data\n'
                              'Get current session user full data. *JWT authentication header required*',
        responses={
            200: EmployeeSerializer(many=False),
            400: ErrorSerializer()
        }
    ))
    def get(self, request):
        try:
            employee = EmployeeModel.objects.get(user=request.user)
        except:
            error = ErrorSerializer()
            error.set_data(status.HTTP_404_NOT_FOUND, 'El usuario actual no cuenta con un perfil')
            return Response(error.get_data(),
                            status=status.HTTP_404_NOT_FOUND)
        return Response(EmployeeSerializer(employee).data)

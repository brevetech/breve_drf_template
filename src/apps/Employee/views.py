import logging
from datetime import datetime

from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.Common.Errors.serializer import ErrorSerializer
from src.paginators import DefaultPagination
from src.apps.Employee.models import EmployeeModel
from src.apps.Employee.serializers import EmployeeSerializer

logger = logging.getLogger('watchtower-logger')


class EmployeeView(viewsets.ModelViewSet):
    """
    # Obtener empleados
    """

    queryset = EmployeeModel.objects.filter(user__is_active=True)
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__frst_name', 'user__last_name', 'user__email', 'dni']
    http_method_names = ['get']
    pagination_class = DefaultPagination


class EmployeeAuthenticatedView(APIView):
    """
    # Retornar metadata de usuario en sesión
    """

    def get(self, request):
        try:
            employee = EmployeeModel.objects.get(user=request.user)
        except:
            error = ErrorSerializer()
            error.set_data(status.HTTP_404_NOT_FOUND, 'El usuario actual no cuenta con un perfil')
            return Response(error.get_data(),
                            status=status.HTTP_404_NOT_FOUND)
        return Response(EmployeeSerializer(employee).data)
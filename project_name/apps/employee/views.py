from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication

from project_name.apps.employee.models import EmployeeModel
from project_name.apps.employee.serializers import EmployeeSerializer
from project_name.common.serializers import ErrorSerializer
from project_name.common.utils import read_docs_md
from project_name.paginators import DefaultPagination


# remember use method_decorator for detailed documentation
@method_decorator(
    name="list",
    decorator=extend_schema(
        description=read_docs_md("endpoints/employee/list"),
        responses={200: EmployeeSerializer(many=True), 400: ErrorSerializer()},
    ),
)
@method_decorator(
    name="retrieve",
    decorator=extend_schema(
        description=read_docs_md("endpoints/employee/retrieve"),
        responses={200: EmployeeSerializer(many=False), 400: ErrorSerializer()},
    ),
)
class EmployeeView(viewsets.ModelViewSet):
    """Main employee viewset"""

    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    queryset = EmployeeModel.objects.filter(user__is_active=True)
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["user__first_name", "user__last_name", "user__email", "dni"]
    http_method_names = ["get"]
    pagination_class = DefaultPagination

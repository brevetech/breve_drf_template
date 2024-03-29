# The serializers and nested serializers added to the app
from rest_framework import serializers

from .models import EmployeeModel


class EmployeeSerializer(serializers.ModelSerializer):
    """Employee serializer"""

    class Meta:
        model = EmployeeModel
        fields = "__all__"

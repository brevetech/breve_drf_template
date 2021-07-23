import serializers as serializers
from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    name = serializers.CharField()
    type = serializers.CharField()
    description = serializers.CharField()
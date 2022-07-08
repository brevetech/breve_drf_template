from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    """Location sample serializer"""

    name = serializers.CharField()
    type = serializers.CharField()
    description = serializers.CharField()

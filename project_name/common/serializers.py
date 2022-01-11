from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    """
    Defines a basic error serializer for
    error responses
    """

    error_code = serializers.IntegerField()
    message = serializers.CharField(max_length=500)

    def set_data(self, error_code, message):
        self.error_code = error_code
        self.message = message

    def get_data(self):
        return {"code_error": self.error_code, "message": self.message}

    class Meta:
        fields = ("error_code", "message")


class MultiErrorSerializer(serializers.Serializer):
    """Defines a basic structure for multi errors responses"""

    errors = serializers.ListField(child=serializers.CharField(max_length=500))
    error_type = serializers.CharField(max_length=100)
    error_code = serializers.IntegerField()

    def set_data(self, error_code, error_type, errors):
        self.error_code = error_code
        self.error_type = error_type
        self.errors = errors

    def get_data(self):
        return {
            "code_error": self.error_code,
            "error_type": self.error_type,
            "errors": self.errors,
        }

    class Meta:
        fields = ("error_code", "error_type", "errors")


class CommonResponseSerializer(serializers.Serializer):
    """
    Defines a basic common response serializer with
    a status field and a message field
    """

    status = serializers.IntegerField()
    message = serializers.CharField(max_length=500)

    def set_data(self, status, message):
        self.status = status
        self.message = message

    def get_data(self):
        return {"status": self.status, "message": self.message}

    class Meta:
        fields = ("code_error", "message")

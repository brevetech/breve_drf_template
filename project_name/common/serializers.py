from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    """Common error serializer"""

    code_error = serializers.IntegerField()
    message = serializers.CharField(max_length=500)

    def set_data(self, code_error, message):
        """sets error data"""
        self.code_error = code_error
        self.message = message

    def get_data(self):
        """gets error data"""
        return {"code_error": self.code_error, "message": self.message}

    class Meta:
        fields = ("code_error", "message")

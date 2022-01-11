
from rest_framework import status
from rest_framework.response import Response

from project_name.common.serializers import ErrorSerializer, MultiErrorSerializer


class BadRequestResponse(Response):
    """
    Defines a bad request response. Init with error message
    """

    def __init__(self, err_message):
        self.status_code = status.HTTP_400_BAD_REQUEST
        error_response = ErrorSerializer({"message": err_message, "error_code": 400})
        super().__init__(error_response.data)


class ValidationErrorResponse(Response):
    """
    Defines a response for validation errors (muli errors). Init with errors list.
    """

    def __init__(self, errors):
        self.status_code = status.HTTP_400_BAD_REQUEST
        error_response = MultiErrorSerializer(
            {
                "errors": errors,
                "error_type": "ValidationError",
                "error_code": 400,
            }
        )
        super().__init__(error_response.data)


class CreatedResponse(Response):
    """
    Defines a created response. Init with serializer data
    """

    def __init__(self, data):
        self.status_code = status.HTTP_201_CREATED
        super().__init__(data)


class NotFoundResponse(Response):
    """
    Defines a created response. Init with error message
    """

    def __init__(self, err_message):
        self.status_code = status.HTTP_404_NOT_FOUND
        error_response = ErrorSerializer({"message": err_message, "error_code": 400})
        super().__init__(error_response.data)


class OkResponse(Response):
    """
    Defines a created response. Init with serializer data
    """

    def __init__(self, data):
        self.status_code = status.HTTP_200_OK
        super().__init__(data)

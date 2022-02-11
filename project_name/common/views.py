from django.http import JsonResponse


def error_404(request, exception):
    """
    Throws a JSON response for NOT_FOUND errors
    :param request: the request
    :return: response
    """
    message = "The requested resource does not exist"
    response = JsonResponse(data={"message": message, "status_code": 404})
    response.status_code = 404
    return response


def error_500(request, *args, **kwargs):
    """
    Throws a JSON response for INTERNAL errors
    :param request: the request
    :return: response
    """
    message = "An internal server error ocurred"
    response = JsonResponse(data={"message": message, "status_code": 500})
    response.status_code = 500
    return response

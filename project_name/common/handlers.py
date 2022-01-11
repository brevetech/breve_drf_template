from rest_framework.views import exception_handler

from {{project_name}}.common.responses import (
    BadRequestResponse,
    ValidationErrorResponse,
    NotFoundResponse,
)
from {{project_name}}.common.utils import extract_errors


def custom_exception_handler(exc, context):
    """
    Defines the exception behaviour for project
    :param(Exception) exc: the exception to throw
    :param(object) context: the context where the exception was thrown
    :return:
    """
    handlers = {
        "ValidationError": _handle_validation_error,
        "Http404": _handle_generic_error,
        "PermissionDenied": _handle_generic_error,
        "NotAuthenticated": _handle_authentication_error,
        "BadRequest": _handle_badrequest_error,
    }

    response = exception_handler(exc, context)

    if response is not None and exc.__class__.__name__ != "ValidationError":
        response.data["status_code"] = response.status_code

    exception_class = exc.__class__.__name__

    return (
        handlers[exception_class](exc, context, response)
        if exception_class in handlers
        else response
    )


def _handle_generic_error(exc, context, response):
    return response


def _handle_authentication_error(exc, context, response):
    response.data = {
        "error": "Authentication required to access this resource",
        "status_code": response.status_code,
    }

    return response


def _handle_badrequest_error(exc, context, response):
    return BadRequestResponse(err_message=str(exc))


def _handle_not_found_error(exc, context, response):
    return NotFoundResponse(err_message=str(exc))


def _handle_validation_error(exc, context, response):
    # if less than 3 fields failed, retrieve verbose multi response
    if len(response.data) <= 3:
        errors = extract_errors(response.data)
        return ValidationErrorResponse(errors=errors)
    # else, return generic response
    else:
        return BadRequestResponse(
            err_message="Multiple errors in model. "
            "Please check your request with the documentation specification"
        )
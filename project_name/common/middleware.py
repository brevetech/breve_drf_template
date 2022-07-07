import json
import logging
import socket
import time

request_logger = logging.getLogger(__name__)


class RequestLogMiddleware:
    """
    Request log middleware class to default logger.
        Source: https://wilspi.com/post/tech/django-middleware-to-log-requests/
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        """"""
        start_time = time.time()
        log_data = {
            "remote_address": request.META["REMOTE_ADDR"],
            "server_hostname": socket.gethostname(),
            "request_method": request.method,
            "request_path": request.get_full_path(),
        }

        # Log every "*/api/vx/*" patterns
        if "/api/v1/" in str(request.get_full_path()):
            req_body = json.loads(request.body.decode("utf-8")) if request.body else {}
            log_data["request_body"] = req_body

        # request passes on to controller
        response = self.get_response(request)

        # add runtime to our log_data
        if response and response["content-type"] == "application/json":
            response_body = json.loads(response.content.decode("utf-8"))
            log_data["response_body"] = response_body
            log_data["response_status"] = response.status_code

        log_data["run_time"] = time.time() - start_time

        log_prefix = (
            "Request made to rest server: "
            if log_data["run_time"] < 3
            else "Long running request made to rest server: "
        )

        request_logger.info(msg=f"{log_prefix}{log_data}")

        return response

    def process_exception(self, request, exception):  # pylint: disable=unused-argument
        """Process unhandled exceptions."""
        try:
            raise exception
        except Exception as exc:  # pylint: disable=broad-except
            request_logger.exception(
                "Unhandled Exception %s at request: %s", exc, request.get_full_path()
            )

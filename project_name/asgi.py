"""
ASGI settings for project_name project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""


from django.core.asgi import get_asgi_application

from project_name.common.utils import get_env_reader, set_settings

env = get_env_reader()

set_settings(env)

application = get_asgi_application()

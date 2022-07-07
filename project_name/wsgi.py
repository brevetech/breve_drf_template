"""
WSGI settings for project_name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""


from django.core.wsgi import get_wsgi_application

from project_name.common.utils import get_env_reader, set_settings

env = get_env_reader()

set_settings(env)

application = get_wsgi_application()

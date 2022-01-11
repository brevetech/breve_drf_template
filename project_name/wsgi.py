"""
WSGI settings for project_name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

from project_name.common.utils import get_env_reader

env = get_env_reader(levels=2)

if sys.argv[1] == 'test':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings.test")
else:
    if env.bool("DEBUG"):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings.dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings.prod")

application = get_wsgi_application()

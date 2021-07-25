"""
ASGI settings for breve_drf_template project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import sys

from django.core.asgi import get_asgi_application

from breve_drf_template.utils import get_env_reader

env = get_env_reader(levels=2)

if sys.argv[1] == 'test':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "breve_drf_template.settings.test")
else:
    if env.bool("DEBUG"):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "breve_drf_template.settings.dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "breve_drf_template.settings.prod")

application = get_asgi_application()

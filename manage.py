#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from {{project_name}}.common.utils import get_env_reader

env = get_env_reader(levels=1)


def main():
    """Run administrative tasks."""
    if sys.argv[1] == 'test':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings.test")
    else:
        if env.bool("DEBUG"):
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings.dev")
        else:
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings.prod")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
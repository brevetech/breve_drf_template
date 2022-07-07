from project_name.settings.base import *  # pylint: disable=W0401, W0614, E0401

ALLOWED_HOSTS = ["localhost"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {"default": env.db("PROD_DB_URL")}  # pylint: disable=E0602

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

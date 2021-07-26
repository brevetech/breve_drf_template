# breve_drf_template
[![Breve Template](https://img.shields.io/badge/breve-template-orange?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MCA3MCI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiNlMDAwNGQ7fS5jbHMtMntmaWxsOiNmZmY7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5SZWN1cnNvIDFsb2dvIHBhcmEgcGVyZmlsIGRlIGNvcnJlbzwvdGl0bGU+PGcgaWQ9IkNhcGFfMiIgZGF0YS1uYW1lPSJDYXBhIDIiPjxnIGlkPSJDYXBhXzEtMiIgZGF0YS1uYW1lPSJDYXBhIDEiPjxyZWN0IGNsYXNzPSJjbHMtMSIgd2lkdGg9IjcwIiBoZWlnaHQ9IjcwIi8+PHBhdGggaWQ9IlN1c3RyYWNjacOzbl8yIiBkYXRhLW5hbWU9IlN1c3RyYWNjacOzbiAyIiBjbGFzcz0iY2xzLTIiIGQ9Ik00Mi41LDU4YTE2LDE2LDAsMCwxLTYuMjUtMS4yN2wtLjY3LS4zdi04LjdIMjUuMzVWMTFIMzUuNThWMjcuMjlsLjY3LS4zYTE2LDE2LDAsMCwxLDE3LjYsMy40NiwxNi4xNywxNi4xNywwLDAsMS01LjEsMjYuMjdBMTYsMTYsMCwwLDEsNDIuNSw1OFptMC0yMi45NGE2LjgxLDYuODEsMCwxLDAsNi43Nyw2LjgzdjBBNi43OSw2Ljc5LDAsMCwwLDQyLjUsMzUuMDVaIi8+PHJlY3QgaWQ9IlJlY3TDoW5ndWxvXzEzIiBkYXRhLW5hbWU9IlJlY3TDoW5ndWxvIDEzIiBjbGFzcz0iY2xzLTIiIHg9IjExLjU2IiB5PSI0Ny43MiIgd2lkdGg9IjEwLjIzIiBoZWlnaHQ9IjEwLjI4Ii8+PC9nPjwvZz48L3N2Zz4=)](https://www.brevetech.com/)
[![forthebadge made-with-python](https://img.shields.io/badge/made_with-python-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![forthebadge django-rest](https://img.shields.io/badge/django-rest_framework-a30000?style=for-the-badge&logo=django)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)

---

A Django Rest Framework base template with custom configurations, intended to save time with some of the boilerplate configuration. Optmized for PyCharm IDE and VSCode. For contrubution feel free to use the `editableVersion` branch; checkout new branch from this branch and pull request to this branch

## Index

- [breve_drf_template](#breve_drf_template)
  - [Index](#index)
  - [Features](#features)
  - [Getting started](#getting-started)
  - [`.env` structure](#env-structure)
  - [Installing additional modules](#installing-additional-modules)
  - [Creating new app](#creating-new-app)
  - [Endpoint clean code architecture](#endpoint-clean-code-architecture)
  - [OpenAPI 3 Schema Documentation](#openapi-3-schema-documentation)
  - [Authentication](#authentication)
  - [CORS Policy](#cors-policy)
  - [Github Actions CI Workflow](#github-actions-ci-workflow)

## Features

- Python 3.9 and Django 3.2.
- `.env` managing with relevant safe variables using [`django-environ`](https://django-environ.readthedocs.io/en/latest/) module.
- `pipfile` requirements modules handling.
- Environment-sensitive settings (`dev`, `test` and `prod`). 
- OpenAPI 3 schema and DocView with full customizable endpoint metadata, using [`drf-spectacular`](https://drf-spectacular.readthedocs.io/en/latest/readme.html). 
- JWT Authentication preconfigured using [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/).
- Default [Github Actions](https://github.com/features/actions) CI workflow.
- `whitenoise` staticfile handling for **Heroku** deploys and similar ones.
- Clean code endpoint architecture.
- Heroku procfile default configuration

## Getting started

To use this template run the following command:

```shell
$ django-admin.py startproject \
  --template=https://github.com/brevetech/breve_drf_template/archive/master.zip \
  --name=Procfile \
  --extension=py,md,env \
  {project_name}
$ cd {project_name}
$ mv idea .idea
$ mv github .github
$ pipenv install --dev
```

This will start a new django project with the template structure. To run the project, you need to set up the `.env` file first.

## `.env` structure

This project uses a `.env` file and the [`django-environ`](https://django-environ.readthedocs.io/en/latest/) module to keep all the sensitive configuration, like secret keys, database URI's or some other credentials off version control. The default `.env` structure includes this variables:
```toml
DEBUG={value}
SECRET_KEY={secret_key}
DEV_DB_URL={dev_db_url}
PROD_DB_URL={prod_db_url}
```
- **DEBUG** (`True`, `False`) will define if debug mode is enabled or not. Use `True` for development and testing purpose and `False` in production environments. This variable also defines which configuration is being used.
- **SECRET_KEY** is the seed used for encryption purposes. Django recommends to keep it off source control. To generate a secret key, you can go to [Djecrety](https://djecrety.ir).
- **DEV_DB_URL** is the development environment database URL. For testing purpose you can use `sqlite:///db.sqlite3` as DEV_DB_URL. If you want to use another database engine, remember to **install** the required package (e.g. `psycopg2` for PostgreSQL databases).
- **PROD_DB_URL** is the production environment database URL. For testing purpose you can use `sqlite:///db.sqlite3` as PROD_DB_URL. If you want to use another database engine, remember to **install** the required package (e.g. `psycopg2` for PostgreSQL databases).

## Installing additional modules

To install a new package, run:

```shell
$ pipenv install {package}
```

This will keep all requirements packages into the `Pipfile`, improving project compatibility across teams and allowing easy use of virtual environments.

To remove a package, run:

```shell
$ pipenv uninstall {package}
```

This will remove the package from the `Pipfile`.

## Creating new app

This template defines a different folder structure for apps, putting them in an `apps` directory inside the project directory. This is only for comfort purposes. Because of this, to create a new app, you need to run this:

```shell
$ mkdir {project_name}/apps/{app_name}
$ python manage.py startapp {app_name} apps/{app_name}
```

After this, you can install the app in the `settings.base`, but using the full app name, not the relative one.

- ~~.app~~
- project_name.apps.app

## Endpoint clean code architecture

This template uses a specific architecture based (kinda) on OOP languages **Clean Architecture**. This is to keep all business logic and validation code off the views code, having cleaner code and more modularization. The files implied here are:

- Serializers:  defines all input and output objects for the endpoints. This serializers can be based on database models `ModelSerializer` or can be full custom serializer `Serializer`. If you want to use different serializers for input and output (e.g. create a join query for output that joins many models or have a different structure than the defined in the model for a create endpoint), you will need to use the `ReadWriteSerializerMixin`.
- Views: defines all endpoints. You can use Function Based Views or Class Based Views (`APIView`, `ViewSet`, `ModelViewSet`).
- Handlers: defines functions with all business logic and validations, database queries and database commands. Use a handler only if you need to redefine a complex logic for the endpoint, otherwise, check if `ModelViewSet` can help.
- Entities: defines input and output objects for the handlers.
- ErrorSerializer: defines the basic error structure for endpoint responses.

Entities, Serializers and handlers are not created when using `python manage.py startapp`, you'll need to create them manually.

The **common** package is meant to store all common access objects, like classes, error serializers, mixins, etc.

## OpenAPI 3 Schema Documentation

This template includes OpenAPI 3 schema documentation, using `.md` files to create rich text descriptions. This descriptions are saved in the **apidocs** folder.

The `index.md` file represents the general schema description. Modify it to edit the schema general description value, like instructions, project objectives, etc. The resting general inforation values are stored in the `SPECTACULAR_SETTINGS` dict in `settings.base`; for more information see [official documentation](https://drf-spectacular.readthedocs.io/en/latest/settings.html).

For every other endpoint you can create a `{endpoint}.md` file in the `apidocs/endpoints/{app}` folder. To load it in the corresponding endpoint, read the file via `read_docs_md()` utils function, and load it via `extend_schema()` function (included in [`drf-spectacular`](https://drf-spectacular.readthedocs.io/en/latest/customization.html#step-2-extend-schema)). Example:

```python
@method_decorator(name='list', decorator=extend_schema(
    summary="Location list",
    # list.md file stores the api description for this endpoint
    description=read_docs_md('endpoints/core/list'),
    responses={
        200: LocationSerializer(many=True),
        400: ErrorSerializer(),
        500: ErrorSerializer()
    }
))
class LocationViewSet(viewsets.ViewSet):
```
## Authentication

This template uses `djangorestframework_simple_jwt` module for JWT Bearer token authentication. 

This module works with a pair of JWT tokens, a `access` one, that is needed as `Authorization` in header of any request, and a `refresh` one that is used to get a new `access` token. Access token lives for 5 minutes by default, and refresh token lives for 24 hours by default; this configuration can be set up as required, see [official documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html). 

The `auth_create` endpoint, for getting an access and refresh token pair with a django user, and the `auth_create_refresh`, that gets a new access token providing a refresh token, are both already exposed and configured by default. 

## CORS Policy

This template uses `django-cors-headers` middleware for cors handling. The configuration is set up in `CORS_ORIGIN_ALLOW_ALL` key at `settings.base`, set `False` as default. Change it to `True` for development purposes when using SPA frontends and third party consumers.

## Github Actions CI Workflow

This template includes a basic Github Actions CI Workflow. It's disabled by default; to enable it, go to `.github/workflows/ci.yml` and toggle comment in all file lines.
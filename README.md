# breve_drf_template

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A base template for **Django Rest Framework**. Less project structuring and more code.

This template includes configuration for: 

-[x] Basic Django Rest Framework environment, with the mostly accepted by the community project structure
-[x] Swagger documentation modularized via **Markdown**
-[x] `.env` file configurations

### Requires Pipenv

You need to have pipenv globally installed and start a fresh new enviroment using the provided `Pipfile`

### Provide a `.env`

Always provide a `.env` file with the keys `DEBUG`, `SECRET_KEY`, `DEV_DB_URL` setting `db.sqlite3` and `PROD_DB_URL` setting `db.sqlite3` 

## Rename the project module

You can use a refactor tool like the ones included in any IDE. Remember to check for the imports in every file.

## How to make a new app?

Mkdir the app folder in `breve_drf_template/apps`, then run `python manage.py startapp <APP_NAME> breve_drf_template/apps/<FOLDER_APP_NAME>`

## Managing dependencies

Always use the `pipenv` commands, to keep your `Pipfile` fresh across the team.
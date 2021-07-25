# breve_drf_template
[![Breve Template](https://img.shields.io/badge/breve-template-orange?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MCA3MCI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiNlMDAwNGQ7fS5jbHMtMntmaWxsOiNmZmY7fTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5SZWN1cnNvIDFsb2dvIHBhcmEgcGVyZmlsIGRlIGNvcnJlbzwvdGl0bGU+PGcgaWQ9IkNhcGFfMiIgZGF0YS1uYW1lPSJDYXBhIDIiPjxnIGlkPSJDYXBhXzEtMiIgZGF0YS1uYW1lPSJDYXBhIDEiPjxyZWN0IGNsYXNzPSJjbHMtMSIgd2lkdGg9IjcwIiBoZWlnaHQ9IjcwIi8+PHBhdGggaWQ9IlN1c3RyYWNjacOzbl8yIiBkYXRhLW5hbWU9IlN1c3RyYWNjacOzbiAyIiBjbGFzcz0iY2xzLTIiIGQ9Ik00Mi41LDU4YTE2LDE2LDAsMCwxLTYuMjUtMS4yN2wtLjY3LS4zdi04LjdIMjUuMzVWMTFIMzUuNThWMjcuMjlsLjY3LS4zYTE2LDE2LDAsMCwxLDE3LjYsMy40NiwxNi4xNywxNi4xNywwLDAsMS01LjEsMjYuMjdBMTYsMTYsMCwwLDEsNDIuNSw1OFptMC0yMi45NGE2LjgxLDYuODEsMCwxLDAsNi43Nyw2LjgzdjBBNi43OSw2Ljc5LDAsMCwwLDQyLjUsMzUuMDVaIi8+PHJlY3QgaWQ9IlJlY3TDoW5ndWxvXzEzIiBkYXRhLW5hbWU9IlJlY3TDoW5ndWxvIDEzIiBjbGFzcz0iY2xzLTIiIHg9IjExLjU2IiB5PSI0Ny43MiIgd2lkdGg9IjEwLjIzIiBoZWlnaHQ9IjEwLjI4Ii8+PC9nPjwvZz48L3N2Zz4=)](https://www.brevetech.com/)
[![forthebadge made-with-python](https://img.shields.io/badge/made_with-python-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![forthebadge django-rest](https://img.shields.io/badge/django-rest_framework-a30000?style=for-the-badge&logo=django)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)

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
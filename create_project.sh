#!/bin/bash
read -p "Enter the project name: " project_name

# render as template all files with .py, .md .env .xml & .iml extension
django-admin startproject --template=https://github.com/brevetech/breve_drf_template/archive/master.zip --name=Procfile --extension=py,md,env,xml,iml $project_name
# move to project folder
cd $project_name
# enable .idea folder package for PyCharm
mv idea .idea
# enable .github folder for Github Actions workflows
mv github .github
# install dependencies
pipenv install --dev
# enable .env file for development environment.
mv .env.sample .env
read -p "Django project successfully created. Remember to update your .env file before running project. Press enter to continue..."

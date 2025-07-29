#!/bin/sh
# entrypoing for docker container

# This script is used to run the Django development server with uvicorn
# It sets the DJANGO_SETTINGS_MODULE environment variable to use the development settings
# and then starts the server.
# Set the settings module to development
export DJANGO_SETTINGS_MODULE=core.settings.dev

# Run the Django development server with uvicorn
uv run manage.py runserver
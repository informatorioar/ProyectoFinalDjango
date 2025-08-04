#!/bin/sh
# Entrypoint for Docker container

# This script prepares the Django application for production deployment
# It runs database migrations, collects static files, and starts the server

set -e  # Exit on any error

echo "Starting Django application setup..."

# Debug: Show current environment variables related to Django
echo "Current DJANGO_SETTINGS_MODULE environment variable: $DJANGO_SETTINGS_MODULE"

# Use the Django settings module from environment variables
# Default to core.settings.prod if not specified
export DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE:-core.settings.prod}
echo "Using Django settings module: $DJANGO_SETTINGS_MODULE"

# Wait for database to be ready
echo "Waiting for database to be ready..."
until uv run python -c "
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '$DJANGO_SETTINGS_MODULE')
django.setup()
from django.db import connection
cursor = connection.cursor()
cursor.execute('SELECT 1')
print('Database connection successful')
" 2>/dev/null; do
    echo "Database is unavailable - sleeping"
    sleep 2
done
echo "Database is ready!"

# Run database migrations
echo "Running database migrations..."
uv run manage.py makemigrations --noinput
uv run manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
uv run manage.py collectstatic --noinput

echo "Setup complete! Starting Django server..."

# Execute the provided command (from CMD in Dockerfile)
exec "$@"
# core/settings/prod.py

from os import getenv

from core.settings.base import *  # noqa: F403

# --- Security ---
# Get SECRET_KEY, DEBUG, and ALLOWED_HOSTS from environment variables.
SECRET_KEY = getenv("SECRET_KEY")
DEBUG = getenv("DEBUG", "False").lower() == "true"  # Should be False in production
ALLOWED_HOSTS = getenv("ALLOWED_HOSTS", "your-production-domain.com").split(",")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": getenv("DB_NAME"),
        "USER": getenv("DB_USER"),
        "PASSWORD": getenv("DB_PASSWORD"),
        "HOST": getenv("DB_HOST", "127.0.0.1"),  # Defaults to localhost
        "PORT": getenv("DB_PORT", "3306"),  # Defaults to MySQL's default port
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

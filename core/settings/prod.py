# core/settings/prod.py

from os import getenv

from environ import env

from core.settings.base import *  # noqa: F403

# --- Security ---
# Get SECRET_KEY, DEBUG, and ALLOWED_HOSTS from environment variables.
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")  # Should be False in production
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["your-production-domain.com"])


# --- Database ---
# Use MySQL for production.
# Configure it using environment variables.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("MYSQL_DATABASE", default="django_db"),
        "USER": env("MYSQL_USER", default="root"),
        "PASSWORD": env("MYSQL_PASSWORD", default="1234"),
        "HOST": env("MYSQL_HOST", default="db-service"),
        "PORT": env("MYSQL_PORT", default="3306"),
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# --- Email ---
# Use a real SMTP service for production emails.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = env("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")


# --- Additional Production Security Settings ---
# It's a good idea to add these for more security.
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": getenv("DB_NAME"),
        "USER": getenv("DB_USER"),
        "PASSWORD": getenv("DB_PASSWORD"),
        "HOST": getenv("DB_HOST", "127.0.0.1"),  # Defaults to localhost
        "PORT": getenv("DB_PORT", "3306"),  # Defaults to MySQL's default port
    }
}

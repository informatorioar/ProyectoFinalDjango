# core/settings/prod.py

from os import getenv

from core.settings.base import *  # noqa: F403

# --- Security ---
# Get SECRET_KEY, DEBUG, and ALLOWED_HOSTS from environment variables.
SECRET_KEY = getenv("SECRET_KEY")
DEBUG = getenv("DEBUG", "False").lower() in (
    "true",
    "1",
    "yes",
)  # Should be False in production
ALLOWED_HOSTS = getenv("ALLOWED_HOSTS", "your-production-domain.com").split(",")


# --- Database ---
# Use MySQL for production.
# Configure it using environment variables.
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

# Google Cloud Storage Configuration
GS_BUCKET_NAME = getenv("GS_BUCKET_NAME", "informatorio")
GOOGLE_APPLICATION_CREDENTIALS = getenv(
    "GOOGLE_APPLICATION_CREDENTIALS", "gcs-informatorio-key.json"
)

# Static files settings for GCS - Override base.py settings
STATIC_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/static/"
STATIC_ROOT = None  # Not needed when using cloud storage
STATICFILES_DIRS = []  # Clear local directories when using cloud storage
GS_DEFAULT_ACL = "publicRead"

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": GS_BUCKET_NAME,
            "location": "media",
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": GS_BUCKET_NAME,
            "location": "static",
        },
    },
}

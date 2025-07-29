# core/settings/dev.py

from core.settings.base import * # noqa: F403

# --- General Development Settings ---
SECRET_KEY = 'django-insecure-4!@#%&*()_+abc1234567890' # Keep a simple key for dev
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "*"]


# --- Database ---
# Simple SQLite database for local development.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', # noqa: F405
    }
}


# --- Email ---
# In development, print emails to the console instead of sending them.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
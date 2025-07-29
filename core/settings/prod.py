# core/settings/prod.py

from core.settings.base import * # noqa: F403

# --- Security ---
# Get SECRET_KEY, DEBUG, and ALLOWED_HOSTS from environment variables.
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG') # Should be False in production
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['your-production-domain.com'])


# --- Database ---
# Use a robust database like PostgreSQL for production.
# Configure it using an environment variable for the database URL.
DATABASES = {
    'default': env.db_url(
        'DATABASE_URL',
        default='postgres://user:password@host:port/dbname'
    )
}
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'


# --- Email ---
# Use a real SMTP service for production emails.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = env('EMAIL_PORT', default=587)
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')


# --- Additional Production Security Settings ---
# It's a good idea to add these for more security.
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
"""Production settings. Requires DJANGO_SECRET_KEY and DJANGO_ALLOWED_HOSTS."""
import os

from .base import *  # noqa: F401,F403

DEBUG = False

# No fallback on purpose: fail loudly if the secret is missing.
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

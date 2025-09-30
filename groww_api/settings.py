# settings.py

from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY (adjust for prod) ---
SECRET_KEY = config("DJANGO_SECRET_KEY", default="CHANGE_ME")
DEBUG = False  # set False in production

ALLOWED_HOSTS = [
    "djangoapi.travestingmoney.com",
    "api.travestingmoney.com",
    "127.0.0.1",
    "localhost",
    # You CAN use "*" but it's safer to be explicit in prod:
    # "*",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_TRUSTED_ORIGINS = [
    "https://djangoapi.travestingmoney.com",
    "https://api.travestingmoney.com",
]

# --- APPS ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",      # <-- add this
    "api",
]

# --- MIDDLEWARE (CORS FIRST) ---
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",   # <-- must be at the top
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "groww_api.urls"
WSGI_APPLICATION = "groww_api.wsgi.application"

# --- DATABASE (you’re using SQLite; fine for dev/small prod) ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- STATIC FILES ---
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"   # for collectstatic in prod

# --- CORS: allow all ---
CORS_ALLOW_ALL_ORIGINS = True
# If you need cookies/Authorization with cross-site requests:
# CORS_ALLOW_CREDENTIALS = True

# Optional: allowed headers/methods (defaults are usually fine)
# CORS_ALLOW_HEADERS = list(default_headers) + ["authorization"]
# CORS_ALLOW_METHODS = list(default_methods)

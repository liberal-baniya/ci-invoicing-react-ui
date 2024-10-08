"""
Django settings for invoiceapp project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-x)n+^tqcw71@pzb_(58l_2%h--_+tu-m=w(lrrconv8%1va816"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "invoice_api",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_WHITELIST = ["http://localhost:3000", "http://127.0.0.1:3000"]

ROOT_URLCONF = "invoiceapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "invoiceapp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "invoicing",
        "ENFORCE_SCHEMA": False,
        "CLIENT": {
            "host": "mongodb+srv://thisisnaman24:rjprivacy24@namanjain.qvaefhl.mongodb.net/",
        },
    }
}

AUTH_USER_MODEL = "invoice_api.User"
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # 'booking_api.authentication.CookieAuthentication',  # Replace with the actual path
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=15
    ),  # Set the lifetime of the access token
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=1
    ),  # Set the lifetime of the refresh token
    "ROTATE_REFRESH_TOKENS": True,  # Whether to rotate refresh tokens
    # "BLACKLIST_AFTER_ROTATION": True,  # Whether to blacklist the old refresh tokens
    "ALGORITHM": "HS256",  # JWT signing algorithm
    "SIGNING_KEY": SECRET_KEY,  # Signing key (must be set to your SECRET_KEY)
    "VERIFYING_KEY": None,  # Key to verify the signature (optional)
    "AUDIENCE": None,  # Audience claim (optional)
    "ISSUER": None,  # Issuer claim (optional)
    "AUTH_HEADER_TYPES": ("Bearer",),  # Authorization header type
    "USER_ID_FIELD": "id",  # Field to use for the user ID
    "USER_ID_CLAIM": "user_id",  # Claim to use for the user ID
    # 'AUTH_TOKEN_CLASSES': ('access',),              # Token classes to use
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",  # HTTP header to use for the token
}
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

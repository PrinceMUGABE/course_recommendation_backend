from datetime import timedelta
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t45i&*2*maqkz=*uwyy@@z$hc-sln0+-3_(%1_)f1w$e)rjz8e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []

APP_NAME = os.environ.get("FLY_APP_COURSE-RECOMMENDATION")
ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    'userApp',
    'courseApp',
    # 'studentApp',
    'studentCourseApp',
]


# Connection string: postgres://postgres:vhLIJCUiGyU04Qo@course-recommendation-d


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'course_recommendation_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'course_recommendation_backend.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.msql',
        'NAME': 'course_recommendation_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




AUTH_USER_MODEL = 'userApp.User'
# Configure Django REST framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Configure Simple JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),  # Access token expiration time
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     # Refresh token expiration time
}

# Configure CORS settings
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Example: Allow requests from a React app running on localhost
    'http://localhost:5000',
    'http://localhost:5500',
]



CORS_ALLOW_ALL_ORGINS = True


# Configure email settings (replace these with your actual email settings)
DEFAULT_FROM_EMAIL = 'no-reply'


# Configure email settings
# Email settings for Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'princemugabe567@gmail.com'
EMAIL_HOST_PASSWORD = 'eayw yfil zfpw hdqy'


# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}



# Postgres cluster course-recommendation-db created
#   Username:    postgres
#   Password:    O96FXMt0kVpEg40
#   Hostname:    course-recommendation-db.internal
#   Flycast:     fdaa:3:36d6:0:1::4
#   Proxy port:  5432
#   Postgres port:  5433
#   Connection string: postgres://postgres:O96FXMt0kVpEg40@course-recommendation-db.flycast:5432


AUTHENTICATION_BACKENDS = [
    'userApp.authentication.CustomAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

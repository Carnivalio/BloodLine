"""
Django settings for bloodline_prj project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!=jrg#(qod$u6c%^!x8((f)hwej1p6ru)xfx$!b6ceuhx37v^8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INCLUDE_REGISTER_URL = True
INCLUDE_AUTH_URLS = True

ALLOWED_HOSTS = ['54.206.126.58', 'localhost', '127.0.0.1']

# Verification email setup
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "cristal.wu17@gmail.com"
###TODO: Not safe here
EMAIL_HOST_PASSWORD = "cristal.wu17"
EMAIL_USE_TLS = True
EMAIL_FROM = "cristal.wu17@gmail.com"

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'bootstrap3',
    'captcha',
    'social_django',
    'bloodline',
    'datetimewidget',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'bloodline_prj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

# Authentication backends Setting
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'bloodline_prj.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


# Google OAuth keys and secret to establish connection from the bloodline app to google service
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "1041450590918-mq5kdrjhe98fpb5bv6f3i8do67r55pm1.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "DgCWdnK2tyE9zUTUdNN4HBri"

# Twitter secret and OAuth keys/secrets to provide connection with BloodLineDonate on twitter
TWITTER_APP_KEY = 'P71z6oUt3Rf4viFJ0ICB9dncR'
TWITTER_APP_SECRET = 'FT7tAPWwFYFHgGLClj0JrcWeGaLZJtTGPrcxMQF4z86VuHvgcs'
TWITTER_OAUTH_TOKEN = '920042363891752960-POj9JCMGsreeGzbkEw46mSGbgOuzUKW'
TWITTER_OAUTH_TOKEN_SECRET = 'yPZ4wc43KBcXdtz7liAT4ijzhbrWj294r2cmmTtYdQzE0'

# Redirect here after login if there's no other query following the url
LOGIN_REDIRECT_URL = '/bloodline'

SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# The location of static files
STATIC_URL = '/static/'

# Default basic routing for bloodline application login, logout, and index/home
LOGIN_URL = 'bloodline_app:login'
LOGOUT_URL = 'bloodline_app:logout'
LOGIN_REDIRECT_URL = 'bloodline_app:home'

# Register custom database into default User database
AUTH_USER_MODEL = 'bloodline.BloodlineUser'

STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
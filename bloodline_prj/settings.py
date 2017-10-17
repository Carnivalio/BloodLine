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
    # 'bloodline.apps.BloodlineConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # 'social.apps.django_app.default',
    'bootstrap3',
    'captcha',
    # ADDITIONAL STARTS
    'social_django',
    'bloodline',
    # ADDITIONAL ENDS
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

    # Social network authentication
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'bloodline_prj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': ['templates'],
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

# SOCIAL_AUTH_PIPELINE = (
#     'social.pipeline.social_auth.social_details',
#     'social.pipeline.social_auth.social_uid',
#     'social.pipeline.social_auth.auth_allowed',
#     'social_auth.backends.pipeline.social.social_auth_user',
#     # 用户名与邮箱关联，文档说可能出现问题
#     # 'social_auth.backends.pipeline.associate.associate_by_email',
#     'social_auth.backends.pipeline.misc.save_status_to_session',
#     'social_auth.backends.pipeline.user.create_user',
#     'social_auth.backends.pipeline.social.associate_user',
#     'social_auth.backends.pipeline.social.load_extra_data',
#     'social_auth.backends.pipeline.user.update_user_details',
#     'social_auth.backends.pipeline.misc.save_status_to_session',
# )

# Authentication backends Setting
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Autentication key pair of Twitter
SOCIAL_AUTH_TWITTER_KEY = 'CSrE5qht3BhI2DBjoVICVqcyO'
SOCIAL_AUTH_TWITTER_SECRET = '	sUw11WVmZZzLcqaKEab7TrJL6BwbPoJsdioEnrUm1ACniIGsTn'

# Authentication key pair of WeChat
SOCIAL_AUTH_WEIXIN_KEY = 'wx4fb***********599'  # 开放平台应用的APPID
SOCIAL_AUTH_WEIXIN_SECRET = 'f1c17************08c0489'  # 开放平台应用的SECRET

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

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "1041450590918-mq5kdrjhe98fpb5bv6f3i8do67r55pm1.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "DgCWdnK2tyE9zUTUdNN4HBri"

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

STATIC_URL = '/static/'

# From Signout project
# APPEND_SLASH = True
LOGIN_URL = 'bloodline_app:login'
LOGOUT_URL = 'bloodline_app:logout'
LOGIN_REDIRECT_URL = 'bloodline_app:home'

AUTH_USER_MODEL = 'bloodline.BloodlineUser'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TWITTER_APP_KEY = 'P71z6oUt3Rf4viFJ0ICB9dncR'
TWITTER_APP_SECRET = 'FT7tAPWwFYFHgGLClj0JrcWeGaLZJtTGPrcxMQF4z86VuHvgcs'
TWITTER_OAUTH_TOKEN = '920042363891752960-POj9JCMGsreeGzbkEw46mSGbgOuzUKW'
TWITTER_OAUTH_TOKEN_SECRET = 'yPZ4wc43KBcXdtz7liAT4ijzhbrWj294r2cmmTtYdQzE0'
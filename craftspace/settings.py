import os
import cloudinary
from datetime import timedelta
from decouple import config
from django.contrib.messages import constants as messages
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_auth',
    'rest_auth.registration',
    'django_filters',
    'djoser',
    'corsheaders',
    'widget_tweaks',
    'cloudinary',
    'phonenumber_field',

    'allauth',
    'allauth.account',

    'core',
    'users',
    'dashboard',
    'products',
    'orders',
    'payments',
]

SITE_ID =1

# force secure https protocol in production environment
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'craftspace.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'craftspace.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': '',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

LOGIN_URL = 'dashboard_login'
LOGIN_REDIRECT_URL = 'dashboard:index'
LOGOUT_URL = 'dashboard_logout'
LOGOUT_REDIRECT_URL = 'dashboard_login'

# mpesa constants
CONSUMER_KEY = config('CONSUMER_KEY')
CONSUMER_SECRET = config('CONSUMER_SECRET')
BS_SHRT_CODE = config('BS_SHORT_CODE')
MPESA_PASSKEY =  config('MPESA_PASSKEY')
TEST_C2B_SHORT_CODE = config('TEST_C2B_SHORT_CODE')

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "auth/password/reset/{uid}/{token}",
    'SERIALIZERS':{
        'user_create': 'users.apiv1.serializers.users_serializer.UserRegistrationSerializer',
        'user': 'users.apiv1.serializers.users_serializer.CustomUserSerializer',
        'current_user': 'users.apiv1.serializers.users_serializer.CustomUserSerializer',
    },
    'LOGIN_FIELD': 'email',
}
cloudinary.config(
    cloud_name='drk0kubip',
    api_key='323542637277415',
    api_secret='-i975ZpUNBKp-4O-2HskFX7OlPU'
)


FRONTEND_HOST = config('FRONTEND_HOST')

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS =True
CORS_ORIGIN_WHITELIST = [FRONTEND_HOST]

AUTH_USER_MODEL = 'users.UserAccount'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
# Phone number validator
PHONENUMBER_DEFAULT_REGION = "KE"
PHONENUMBER_DB_FORMAT = "NATIONAL"

# jwt settings
SIMPLE_JWT = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': timedelta(hours=1),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
}

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST=config('EMAIL_HOST')
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
EMAIL_PORT=config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = True


MESSAGE_TAGS = {
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}
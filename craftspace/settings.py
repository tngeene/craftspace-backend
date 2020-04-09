import os
import cloudinary
from datetime import timedelta
from decouple import config
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
    'rest_framework_simplejwt',
    'django_filters',
    'djoser',
    'corsheaders',
    'widget_tweaks',
    'cloudinary',

    'allauth',
    'allauth.account',

    'core',
    'users',
    'dashboard',
    'products',
    'orders',
]

SITE_ID =1

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
# uncomment to use sendgrid
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS')
# EMAIL_PORT = config('EMAIL_PORT')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'SERIALIZERS':{
        'user_create': 'users.apiv1.serializers.users_serializer.UserRegistrationSerializer',
        'user': 'users.apiv1.serializers.users_serializer.CustomUserSerializer',
        'current_user': 'users.apiv1.serializers.users_serializer.CustomUserSerializer',
    },
    'LOGIN_FIELD': 'email',
    # 'SEND_ACTIVATION_EMAIL': True,
    # 'SEND_CONFIRMATION_EMAIL': True,
    # 'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    # 'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    # 'LOGOUT_ON_PASSWORD_CHANGE': True,
    # 'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    # 'TOKEN_MODEL': 'users.models.Token',
    # 'ACTIVATION_URL': 'auth/activate/{uid}/{token}',
}
cloudinary.config(
    cloud_name='drk0kubip',
    api_key='323542637277415',
    api_secret='-i975ZpUNBKp-4O-2HskFX7OlPU'
)


FRONTEND_HOST = config('FRONTEND_HOST')

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS =True
CORS_ORIGIN_WHITELIST = [
    FRONTEND_HOST,
    'http://localhost:3000',
]

AUTH_USER_MODEL = 'users.UserAccount'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'users.helpers.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

# jwt settings
SIMPLE_JWT = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': timedelta(hours=1),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
}
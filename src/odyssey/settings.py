"""
Django settings for odyssey project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b6!v3a3yfozbwpk79xe%55%pr&jy8gj)9#gglnhu0tp0_=b$03'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'filebrowser',

    'odyssey.userext',
    'odyssey.blog',
    'odyssey.media',
    'odyssey.info',
    'odyssey.toolbox',

    'tinymce',

    #'rest_framework',
    #'rest_framework.authtoken',
    #'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    # 'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'odyssey.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'odyssey.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

SENDFILE_BACKEND = 'sendfile.backends.simple'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_EMAIL_FIELD = 'email'
ACCOUNT_LOGOUT_ON_GET = True

AUTH_USER_MODEL = 'userext.User'

#REST_AUTH_SERIALIZERS = {
#    "USER_DETAILS_SERIALIZER": "userext.serializers.UserSerializer",
#}

#REST_AUTH_REGISTER_SERIALIZERS = {
#    "REGISTER_SERIALIZER": "users.serializers.CustomRegisterSerializer",
#}

#https://dev.to/callmetarush/the-django-rest-custom-user-model-and-authentication-5go9



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

SERVER = 'http://127.0.0.1:8000'

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = ''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
UPLOAD_DIR = os.path.join(BASE_DIR, 'media')


#CORS_ORIGIN_ALLOW_ALL = True
#CORS_ALLOW_CREDENTIALS = True
#CORS_ORIGIN_WHITELIST = (
#    # TODO - set this properly for production
#    'http://127.0.0.1:8080',
#    'http://127.0.0.1:8000',
#    'http://localhost:8080',
#    'http://localhost:8000',
#)

#REST_FRAMEWORK = {
#    'DEFAULT_PERMISSION_CLASSES': (
#        'rest_framework.permissions.IsAuthenticated',0
#
#        # 'rest_framework.permissions.IsAdminUser',
#        # 'rest_framework.permissions.IsAuthenticated',
#        # 'rest_framework.permissions.AllowAny',
#    ),
#    'TEST_REQUEST_RENDERER_CLASSES': (
#        'rest_framework.renderers.MultiPartRenderer',
#        'rest_framework.renderers.JSONRenderer',
#        'rest_framework.renderers.TemplateHTMLRenderer'
#    ),
#    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#        'rest_framework.authentication.SessionAuthentication',
#        'rest_framework.authentication.BasicAuthentication',
#    ),
#    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#    'PAGE_SIZE': 20,
#}

#from datetime import timedelta

#JWT_AUTH = {
#    'JWT_ALLOW_REFRESH': True,
#    'JWT_EXPIRATION_DELTA': timedelta(hours=1),
#    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
#}


PAGE_SIZE = 5

TINYMCE_JS_URL = STATIC_URL + 'lib/tinymce/tinymce.min.js'
#TINYMCE_DEFAULT_CONFIG = {
#    'plugins': "codesample,table,paste,searchreplace,code,advcode,image,imagetools,wordcount,visualchars,visualblocks,toc,quickbars,preview,pageembed,pagebreak,nonbreaking,media,lists,advlist,link,linkchecker,insertdatetime,hr,fullscreen,formatpainter,emoticons,directionality,charmap,casechange,bbcode",
#    # 'theme': "advanced",
#    'cleanup_on_startup': True,
#    'custom_undo_redo_levels': 10,
#}
TINYMCE_DEFAULT_CONFIG = {
    'height': 800,
    'width': 1200,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}
# INYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = True
TINYMCE_EXTRA_MEDIA = {
    'css': {
        'all': [
        ],
    },
    'js': [
    ],
}
TINYMCE_FILEBROWSER = True

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_URL_FILEBROWSER_MEDIA = '/static/filebrowser/'
FILEBROWSER_PATH_FILEBROWSER_MEDIA = BASE_DIR
FILEBROWSER_DEFAULT_SORTING_BY = 'filename_lower'
FILEBROWSER_DEFAULT_SORTING_ORDER = 'asc'
FILEBROWSER_MAX_UPLOAD_SIZE = 1024*1024*100
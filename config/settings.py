"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path
import dj_database_url
import django_heroku

PYTHONUNBUFFERED = 0
DEBUG = False

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['*']

# Generally avoid wildcards(*). However since Heroku router provides hostname validation it is ok

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--52z56g1q)skhx7ujys8hogyy6u54#e7rbbzi7o@(n%*qs86mp'

# SECURITY WARNING: don't run with debug turned on in production!


# SECURITY WARNING: don't run with debug turned on in production!

# Application definition

DJANGO_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

]
LOCAL_APPS = [
    'core.apps.CoreConfig',
    'users.apps.UsersConfig',
    'meeting',
]
THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    "rest_framework_simplejwt.token_blacklist",
    'rest_framework_simplejwt',
    "whitenoise.runserver_nostatic",

    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',

    'drf_spectacular',
    'phonenumber_field',
    'simple_history',
    "corsheaders",
    'django_extensions',
    'django_countries',

]
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

        }

    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MAX_CONN_AGE = 600

if "DATABASE_URL" in os.environ:
    # Configure Django for DATABASE_URL environment variable.
    DATABASES["default"] = dj_database_url.config(
        conn_max_age=MAX_CONN_AGE, ssl_require=True)

    # Enable test database if found in CI environment.

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Django-extensions Graph
GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}

# CorsHeader
CORS_ALLOW_ALL_ORIGINS=True

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [BASE_DIR / "static"]  # new

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'

SITE_ID = 1
# Enable WhiteNoise's GZip compression of static assets.
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# Authentication Settings for Django Rest Framework
DEFAULT_AUTO_FIELD = 'uuid'
AUTH_USER_MODEL = "users.User"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "users.serializers.Dj_Rest_Auth_Custom_User_Serializer",
    "PASSWORD_RESET_SERIALIZER": "users.serializers.CustomPasswordResetSerializer",
}
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'users.serializers.CustomRegisterSerializer',
    'USER_DETAILS_SERIALIZER': 'users.serializers.UserSerializer',

}
#
AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
)
REST_USE_JWT = True
REST_AUTH_PW_RESET_USE_SITES_DOMAIN = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = False

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_TOKEN_CLASSES": (
        "rest_framework_simplejwt.tokens.AccessToken",
        "rest_framework.authentication.SessionAuthentication",
    ),
}

LOGIN_URL = "http://localhost:3000/login"
SITE_URL = "http://localhost:8000"
FRONTEND_URL = "http://localhost:3000"
REST_AUTH_USE_SITES_DOMAIN = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Lokkna from Nasir"
SOCIALACCOUNT_PROVIDERS = {
    "facebook": {
        "METHOD": "oauth2",
        "SDK_URL": "//connect.facebook.net/{locale}/sdk.js",
        "SCOPE": ["email", "public_profile", "user_gender"],
        "AUTH_PARAMS": {"auth_type": "reauthenticate"},
        "INIT_PARAMS": {"cookie": True},
        "FIELDS": [
            "id",
            "email",
            "first_name",
            "last_name",
            "gender",
        ],
        "EXCHANGE_TOKEN": True,
        "LOCALE_FUNC": "path.to.callable",
        "VERIFIED_EMAIL": False,
        "VERSION": "v7.0",
    }
}

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # "rest_framework.authentication.SessionAuthentication",
    ),
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'Thunder Meets API',
    'DESCRIPTION': 'The Meeting App For Ultimate Productivity',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': True,

    # OTHER SETTINGS
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
USE_I18N = True
DEBUG_PROPAGATE_EXCEPTIONS = True
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Thunder Meets Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Thunder Meets",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Thunder Meets",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "logo.jpeg",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": 'logo.jpeg',

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the thunder meets admin",

    # Copyright on the footer
    "copyright": "",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://github.com/nasir733/Thunder-Meets-Backend/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-info",
    "accent": "accent-warning",
    "navbar": "navbar-info navbar-dark",

    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-lightblue",

    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "cyborg",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }

}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Test Runner Config
django_heroku.settings(locals())
# Use HerokuDiscoverRunner on Heroku CI

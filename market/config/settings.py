"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from django.urls import reverse_lazy
from dotenv import dotenv_values

import dj_database_url
import pygments.formatters

config = dotenv_values(os.path.join("..", ".env"))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-=e-i4dlx_qq&ra7un4)u8bdr#08q)gc_*yyy4@7--kt(0(p#!("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django_extensions",
    "mptt",
    "taggit",
    "django_jinja",
    "django_mptt_admin",
    "django_filters",
    "phonenumber_field",
    "django_celery_results",
    "django_celery_beat",
    "stripe",
    "products",
    "shops",
    "users",
    "reviews",
    "cart",
    "viewings",
    "orders",
    "comparison",
    "imports",
    "settings",
    "payments",

]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "DIRS": [Path(BASE_DIR).joinpath("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            # django-jinja defaults
            "match_extension": ".j2",
            "match_regex": None,
            "app_dirname": "templates",
            "constants": {},
            "globals": {},
            "context_processors": [
                "context_processors.categories_context.categories",
                "context_processors.properties_context.properties",
                "context_processors.cart_context.cart",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
            ],

        }
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {"default": dj_database_url.parse(config["DATABASE_URL"])}

REDIS_URL = config["REDIS_URL"]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

# Internationalization
USE_I18N = True
LANGUAGES = [
    ('ru', 'Русский'),
    ('en', 'English')
]
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale/"),
]

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

INTERNAL_IPS = [
    "127.0.0.1"
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'users.User'

FIXTURE_DIRS = [
    BASE_DIR / 'fixtures',
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Данные для отправки сообщений на почту пользователя.
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

CART_SESSION_ID = 'cart'
DELIVERY_SESSION_ID = 'delivery_id'

# The key for comparing products
COMPARE_SESSION_ID = "compare"

# Always use IPython for shell_plus
SHELL_PLUS = "ipython"
SHELL_PLUS_PRINT_SQL = True

# To disable truncation of sql queries use
SHELL_PLUS_PRINT_SQL_TRUNCATE = None

# Specify sqlparse configuration options when printing sql queries to the console
SHELL_PLUS_SQLPARSE_FORMAT_KWARGS = dict(
    reindent_aligned=True,
    truncate_strings=500,
)

# Specify Pygments formatter and configuration options when printing sql queries to the console
SHELL_PLUS_PYGMENTS_FORMATTER = pygments.formatters.TerminalFormatter
SHELL_PLUS_PYGMENTS_FORMATTER_KWARGS = {}

LOGIN_URL = reverse_lazy('users:login_user')

# CELERY
CELERY_BROKER_URL = REDIS_URL  # для rabbitmq, поменяйте адрес брокера на amqp://guest:guest@127.0.0.1:5672
CELERY_TASK_TRACK_STARTED = True  # запускает трекинг задач Celery

# Планировщик задач

# Celery настроен на использование планировщика из базы данных
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

CELERY_BROKER_TRANSPORT_OPTION = {'visibility_timeout': 3600}  # время ожидания видимости 1 час
CELERY_RESULT_BACKEND = 'django-db'  # указание для django_celery_results куда записывать результат выполнения задач
CELERY_ACCEPT_CONTENT = ['application/json']  # это тип содержимого, разрешенный к получению
CELERY_TASK_SERIALIZER = 'json'  # это строка, используемая для определения метода сериализации по умолчанию
CELERY_RESULT_SERIALIZER = 'json'  # является типом формата сериализации результатов

CELERY_TASK_DEFAULT_QUEUE = 'default'  # celery будет использовать это имя очереди

# Данные почты получателя уведомлений о проведённом импорте
RECIPIENTS_EMAIL = ['service.megano@gmail.com']   # список получателей по умолчанию
DEFAULT_FROM_EMAIL = config['EMAIL_HOST_USER']  # почта администратора
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# для подключения к системе платежей
STRIPE_PUBLISHABLE_KEY = config['STRIPE_PUBLISHABLE_KEY']
STRIPE_SECRET_KEY = config['STRIPE_SECRET_KEY']
STRIPE_WEBHOOK_KEY = config['STRIPE_WEBHOOK_KEY']

CELERY_TASK_NAME_1 = 'Импорт товаров'

# Устанавливаем количество записей для страниц, использующих пагинацию
PAGINATE_BY = 3

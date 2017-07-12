
# Django settings for {{ project_name }} project.

from django.conf.global_settings import *    # pylint: disable=W0614,W0401
import os
import sys


try:
    virtualenv_root = os.environ['VIRTUAL_ENV']
except KeyError:
    sys.stderr.write('Error: virtualenv does not activated.\n')
    sys.exit(1)

VAR_ROOT = os.path.join(virtualenv_root, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))


TIME_ZONE = 'Asia/Vladivostok'

LANGUAGE_CODE = 'ru'

USE_I18N = True

USE_L10N = True

USE_TZ = False

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1

MEDIA_ROOT = os.path.join(VAR_ROOT, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

SECRET_KEY = '{{ secret_key }}'


GRAPPELLI_INSTALLED = True
TINYMCE_SETUP_JS = 'mezzanine/js/tinymce_setup.js'
JQUERY_UI_FILENAME = 'jquery-ui-1.8.24.min.js'
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
TESTING = False
SLUGIFY = 'slugify.slugify_ru'

USE_MODELTRANSLATION = False

ROOT_URLCONF = 'urls'
TEMPLATE_PATH = os.path.join(PROJECT_ROOT, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "mezzanine.conf.context_processors.settings",
                "mezzanine.pages.context_processors.page",
            ],
        },
    },
]

INSTALLED_APPS = (
    'django_comments',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",

    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.forms",
    'base_api',
    'sample_1',
    'sample_2',
    'sample_3',
)

MIDDLEWARE_CLASSES = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

AUTHENTICATION_BACKENDS += (
)

#==============================================================================
# App settings
#==============================================================================

OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)


JSON_SIZE = 5000
JSON_LEN = 4000

# Specifically for FileBrowser
if not os.path.exists(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)
if not os.path.exists(os.path.join(MEDIA_ROOT, 'uploads')):
    os.mkdir(os.path.join(MEDIA_ROOT, 'uploads'))

try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())

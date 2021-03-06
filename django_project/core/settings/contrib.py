from .base import *  # noqa

# Extra installed apps that needs to be added before others
INSTALLED_APPS = (
    'test_without_migrations',
    'grappelli',
    'formtools',
) + INSTALLED_APPS

INSTALLED_APPS += (
    # add third party (pip installed) apps here
    'corsheaders',
)

MIGRATION_MODULES = {'accounts': 'core.migration'}

GRAPPELLI_ADMIN_TITLE = 'Site administration panel'

STOP_WORDS = (
    'a', 'an', 'and', 'if', 'is', 'the', 'in', 'i', 'you', 'other',
    'this', 'that', 'to',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Easy-thumbnails options
THUMBNAIL_SUBDIR = 'thumbnails'
THUMBNAIL_ALIASES = {
    '': {
        'entry': {'size': (50, 50), 'crop': True},
        'medium-entry': {'size': (100, 100), 'crop': True},
        'large-entry': {'size': (400, 300), 'crop': True},
        'thumb300x200': {'size': (300, 200), 'crop': True},
    },
}

# Pipeline related settings

INSTALLED_APPS += (
    'crispy_forms',
    'django_extensions',
    'pipeline',)

MIDDLEWARE += [
    # For rosetta localisation
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_METHODS = (
    'GET'
)

DEFAULT_FILE_STORAGE = (
    'django_hashedfilenamestorage.storage.HashedFilenameFileSystemStorage')

# use underscore template function
PIPELINE_TEMPLATE_FUNC = '_.template'

# enable cached storage - requires uglify.js (node.js)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Contributed / third party js libs and css for pipeline compression
# For hand rolled js/css for this app, use project.py

PIPELINE = {
    # These get enabled in prod.py
    'JS_COMPRESSOR': None,
    'CSS_COMPRESSOR': None,
    'PIPELINE_ENABLED': False,
    'JAVASCRIPT': {
        'contrib': {
            'source_filenames': (
                # 'js/.js',
            ),
            'output_filename': 'js/contrib.js',
        }
    },
    'STYLESHEETS': {}
}

# Django-allauth related settings

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    # 'allauth.account.auth_backends.AuthenticationBackend',
)

# INSTALLED_APPS += (
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount'
# )

# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_USERNAME_VALIDATORS = None
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_SIGNUP_FORM_CLASS = 'base.forms.SignupForm'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None

# Set default template pack
CRISPY_TEMPLATE_PACK = 'bootstrap4'
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

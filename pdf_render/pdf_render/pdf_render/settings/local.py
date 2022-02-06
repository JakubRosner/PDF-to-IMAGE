from .base import *  # noqa
from datetime import timedelta

INSTALLED_APPS += ["drf_yasg", "silk"]  # noqa

SIMPLE_JWT = {"ACCESS_TOKEN_LIFETIME": timedelta(days=365)}

MIDDLEWARE += ["silk.middleware.SilkyMiddleware"]  # noqa

REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] += (  # noqa
    "rest_framework.authentication.SessionAuthentication",
)

LANGUAGE_CODE = "en"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "DEBUG",  # change debug level as appropriate
            "propagate": False,
        },
        "qinspect": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },  # noqa
    },
}


REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (  # noqa
    "rest_framework.renderers.BrowsableAPIRenderer",
    "rest_framework.renderers.JSONRenderer",
)

MEDIA_ROOT = "/tmp"
MEDIA_URL = "/files/"

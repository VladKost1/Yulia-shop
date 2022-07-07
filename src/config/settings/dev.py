import os

from config.settings.base import *

DEBUG = True

CURRENT_ENV = "DEV"
print(CURRENT_ENV)

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",  # noqa
            "NAME": os.environ["POSTGRES_DB"],  # noqa
            "USER": os.environ["POSTGRES_USER"],    # noqa
            "PASSWORD": os.environ["POSTGRES_PASSWORD"],    # noqa
            "HOST": os.environ["POSTGRES_HOST"],    # noqa
            "PORT": os.environ["POSTGRES_PORT"],    # noqa
        },
    }

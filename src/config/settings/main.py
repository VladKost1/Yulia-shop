import os

from config.settings.base import *
from config.settings.base import BASE_DIR

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "ec2-13-40-36-138.eu-west-2.compute.amazonaws.com"
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = "/static/"

CURRENT_ENV = "MAIN"
print(CURRENT_ENV)

DATABASES = {
    # "default_pg": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": os.environ["POSTGRES_DB"],  # noqa:
    #     "USER": os.environ["POSTGRES_USER"],  # noqa:
    #     "PASSWORD": os.environ["POSTGRES_PASSWORD"],  # noqa:
    #     "HOST": os.environ["POSTGRES_HOST"],  # noqa:
    #     "PORT": os.environ["POSTGRES_PORT"],  # noqa:
    # },
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}
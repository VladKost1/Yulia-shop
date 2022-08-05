from config.settings.base import *

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
]

CURRENT_ENV = "STAGE"
print(CURRENT_ENV)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],  # noqa:
        "USER": os.environ["POSTGRES_USER"],  # noqa:
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],  # noqa:
        "HOST": os.environ["POSTGRES_HOST"],  # noqa:
        "PORT": os.environ["POSTGRES_PORT"],  # noqa:
    },
}

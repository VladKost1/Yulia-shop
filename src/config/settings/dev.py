from config.settings.base import *  # noqa
import os


DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
]

CURRENT_ENV = "DEV"
print(CURRENT_ENV)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_URL = "/static/"

# if os.environ.get("GITHUB_WORKFLOW"):  # noqa
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
# else:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.postgresql",
#             "NAME": os.environ["POSTGRES_DB"], # noqa
#             "USER": os.environ["POSTGRES_USER"],    # noqa
#             "PASSWORD": os.environ["POSTGRES_PASSWORD"],    # noqa
#             "HOST": os.environ["POSTGRES_HOST"],    # noqa
#             "PORT": os.environ["POSTGRES_PORT"],    # noqa
#         },
#     }

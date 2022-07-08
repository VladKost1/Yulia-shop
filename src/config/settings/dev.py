from config.settings.base import *  # noqa

DEBUG = True

CURRENT_ENV = "DEV"
print(CURRENT_ENV)

if os.environ.get("GITHUB_WORKFLOW"):  # noqa
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "localhost",
            "PORT": "5433",
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
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",  # noqa
        },
    }

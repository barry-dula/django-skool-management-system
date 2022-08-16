from .base import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "info@skool-system.com"
DOMAIN = config("DOMAIN")
SITE_NAME = "school management system"


# DATABASES = {
#     "default": {
#         "ENGINE": config("POSTGRES_ENGINE"),
#         "NAME": config("DB_NAME"),
#         "USER": config("POSTGRES_USER"),
#         "PASSWORD": config("POSTGRES_PASSWORD"),
#         "HOST": config("PG_HOST"),
#         "PORT": config("PG_PORT"),
#     }
# }

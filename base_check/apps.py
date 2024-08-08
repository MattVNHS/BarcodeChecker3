from django.apps import AppConfig


class BaseCheckConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_check'

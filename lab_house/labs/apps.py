from allauth.account.signals import user_signed_up
from django.apps import AppConfig
from django.dispatch import receiver



class LabsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'labs'
    verbose_name = 'Лабораторные'

    def ready(self):
        import labs.signals


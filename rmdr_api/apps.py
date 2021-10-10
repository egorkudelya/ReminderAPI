from django.apps import AppConfig


class RmdrApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rmdr_api'

    def ready(self):
        print('The scheduler is on')
        from .scheduler import updater
        updater.start()
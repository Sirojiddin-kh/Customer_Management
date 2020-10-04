from django.apps import AppConfig


class AcountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals

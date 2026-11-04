from django.apps import AppConfig


class CatalogConfig(AppConfig):
    name = 'catalog'

    def ready(self):
        # Connect the signal handlers in signals.py.
        from . import signals  # noqa: F401

from django.apps import AppConfig


class DjstripeAppConfig(AppConfig):
    name = "djstripe"

    def ready(self):
        # Much like registering signal handlers. We import this module so that its registrations get picked up
        # the NO QA directive tells flake8 to not complain about the unused import
        from . import event_handlers  # NOQA

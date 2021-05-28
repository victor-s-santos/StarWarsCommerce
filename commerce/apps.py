from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class CommerceConfig(AppConfig):
    name = 'commerce'

    def ready(self):
        import commerce.signals

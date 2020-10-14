from django.apps import AppConfig


class ForestConfig(AppConfig):
    name = 'Forest'

    def ready(self):
    	import Forest.signals


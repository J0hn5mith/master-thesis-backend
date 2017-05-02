from django.apps import AppConfig


class AlarmConfig(AppConfig):
    name = 'alarm'
    verbose_name = "Alarm"

    def ready(self):
        import alarm.signals #noqa

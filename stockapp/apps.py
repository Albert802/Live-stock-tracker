from django.apps import AppConfig

class StockappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stockapp'

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

    def ready(self):
        from django_celery_beat.models import PeriodicTask, IntervalSchedule
        from django.db.utils import OperationalError
        from django.core.exceptions import ImproperlyConfigured

        try:
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=5,
                period=IntervalSchedule.SECONDS,
            )

            PeriodicTask.objects.get_or_create(
                interval=schedule,
                name='Update stock prices every 5 sec',
                task='dashboard.tasks.update_stock_prices_task',
            )
        except (OperationalError, ImproperlyConfigured):
            # This avoids errors on first migration
            pass



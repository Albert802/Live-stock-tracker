from celery import shared_task
from .fetch_prices import update_all_stocks

@shared_task(bind=True)
def update_stock_prices_task(self):
    try:
        update_all_stocks()
    except Exception as e:
        self.retry(exc=e, countdown=10, max_retries=3)
        print(f"❌ Celery task failed: {e}")

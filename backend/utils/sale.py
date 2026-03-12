from django.utils import timezone
from datetime import timedelta

def default_delivery_date(instance):
    return timezone.now() + timedelta(days=5)
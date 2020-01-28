import datetime
from django.utils import timezone


def check_shopping_event_time(shopping_date):
    timediff = timezone.now() - shopping_date
    if timediff.total_seconds() > 180:
        return False
    return True
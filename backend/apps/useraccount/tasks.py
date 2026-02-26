from celery.utils.log import get_task_logger
from celery import shared_task
from django.contrib.auth import get_user_model
from django.contrib.gis.geoip2 import GeoIP2
from user_agents import parse
from datetime import timedelta
from django.utils import timezone

from .models import UserLoginTrack

User = get_user_model()
logger = get_task_logger(__name__)


@shared_task
def track_user_login(**kwargs):
    ip = kwargs["ip_address"]
    ua_string = kwargs.pop("ua_string", "")
    kwargs["user_agent"] = ua_string

    user_agent = parse(ua_string)

    kwargs["is_active"] = True
    kwargs["browser_name"] = user_agent.browser.family
    kwargs["browser_version"] = user_agent.browser.version_string
    kwargs["platform"] = user_agent.os.family
    kwargs["device"] = user_agent.device.family

    try:
        geoip = GeoIP2()
        location_info = geoip.city(ip)
        kwargs["city"] = location_info["city"]
        kwargs["country"] = location_info["country_name"]
    except Exception:
        pass

    user = User.objects.get(id=kwargs["user"])
    kwargs["user"] = user
    
    user_login_track = UserLoginTrack(**kwargs)
    user_login_track.save()
    task_message = f"User {user.username}'s track added"
    logger.info(task_message)


@shared_task
def daily_user_login_track_cleanup():
    threshold = timezone.now() - timedelta(days=30)
    deleted_count, _ = UserLoginTrack.objects.filter(created_at__lt=threshold).delete()
    
    task_message = f"Deleted {deleted_count} old login records"
    
    logger.info(task_message)
    
    return task_message
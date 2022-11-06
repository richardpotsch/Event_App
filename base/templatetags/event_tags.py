import datetime
from django import template

from base.models import EventResponse

register = template.Library()

@register.simple_tag
def get_latest_response(event_id, user_id):
    latest_response = EventResponse.objects.filter(
        user_id=user_id,
        event_id=event_id
    ).order_by('-response_date').first()
    if latest_response:
        return str(latest_response)
    return None

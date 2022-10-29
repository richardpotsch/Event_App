from django.contrib import admin

# Register your models here.
from django.contrib import admin
from base.models import Event, Message, Type_event, EventResponse

admin.site.register(Type_event)
admin.site.register(Event)
admin.site.register(Message)
admin.site.register(EventResponse)

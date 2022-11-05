from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Q

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Type_event(models.Model):
    objects = None
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
#new*
class Event(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    active = models.BooleanField()
    type_event = models.ForeignKey(Type_event, on_delete = models.PROTECT)
    description = models.TextField(null=True, blank=True)
    place = models.TextField(null=True, blank=True)
    price = models.DecimalField(validators=[MaxValueValidator(10000)], max_digits=7, decimal_places=2)
    ticked_side = models.IntegerField(blank=True) #max_lenght=4
    ticked_stand = models.IntegerField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_active = models.DateField(blank=True)
    date_deactive = models.DateField(blank=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField(blank=True)
    #date= models.DateField(blank=True)

    class Meta:
        ordering = ['-date_created', 'name' ]

    def __str__(self):
        result = f"{self.name} - {self.description[0:50]}"
        return result

    # Event.recommended_events
    def recommended_events(self):
        return Event.objects.filter((Q(type_event = self.type_event) ) & ~Q(id = self.id))

class EventResponse(models.Model):
    class ResponseTypes(models.TextChoices):
        YES = 'yes'
        MAYBE = 'maybe'
        NOT_INTERESTED = 'not interested'
    response_date = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete = models.PROTECT)
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    response_type = models.CharField(max_length=21, choices= ResponseTypes.choices, default=ResponseTypes.YES)

    def __str__(self):
        result = f"User {self.user_id}, responded {self.response_type} for event_id {self.event_id}."
        return result

class Message(models.Model):
    Multipleobjects = None
    objects = None
    message = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return self.message[0:50]



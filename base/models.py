from django.core.validators import MaxValueValidator
from django.db import models

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
    ticked_side = models.IntegerField() #max_lenght=4
    ticked_stand = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_active = models.DateTimeField()
    date_deactive = models.DateTimeField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()


    class Meta:
        ordering = ['-date_created', 'name' ]

    def __str__(self):
        return self.name

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



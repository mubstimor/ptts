from django.db import models
from django import forms

class Route(models.Model):
    #route_id = models.AutoField(primary_key=True)
    route_name = models.CharField(max_length=30)
    route_start = models.CharField(max_length=25)
    route_end = models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now_add=True, blank=False)

    def __unicode__(self):
        return self.route_name

class Bus(models.Model):
    license_number = models.CharField(max_length=12)
    imeib = models.CharField(max_length=25)
    route_id = models.ForeignKey(Route, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=False)

    def __unicode__(self):
        return self.license_number

class Route_Stop(models.Model):
    stop_name = models.CharField(max_length=25)
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    route = models.ForeignKey(Route, related_name='stops')

    def __unicode__(self):
        return self.stop_name

class coordinate(models.Model):
    imei = models.CharField(max_length=25)
    latitude = models.CharField(max_length=25)
    longitude =models.CharField(max_length=25)
    route_id = models.ForeignKey(Route, null=True, blank=True)
    bus_id = models.ForeignKey(Bus, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=False)

    def __unicode__(self):
        return self.imei

class Contact(models.Model):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()

    @property
    def __unicode__(self):
        return self.subject
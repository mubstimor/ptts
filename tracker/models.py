from django.db import models
from django.forms import ModelForm
from django import forms
from django.forms import ModelForm

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
    route = models.ForeignKey(Route)
    date_added = models.DateTimeField(auto_now_add=True, blank=False)

    def __unicode__(self):
        return self.license_number

class Route_Stop(models.Model):
    stop_name = models.CharField(max_length=25)
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    route = models.ForeignKey(Route)

    def __unicode__(self):
        return self.stop_name

class Cordinate(models.Model):
    imei = models.CharField(max_length=25)
    latitude = models.CharField(max_length=25)
    longitude =models.CharField(max_length=25)
    date_added = models.DateTimeField(auto_now_add=True, blank=False)

    def __unicode__(self):
        return self.latitude

class Contact(models.Model):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()

    @property
    def __unicode__(self):
        return self.subject
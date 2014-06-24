from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tracker.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'route_name', 'route_start','route_end')

class RouteStopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route_Stop
        fields = ('id', 'stop_name', 'latitude','longitude')

class BusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = ('id', 'license_number','imei', 'route')

class CordinateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =coordinate
        fields = ('bus', 'latitude', 'longitude','date_added')

class StopSerializer(serializers.ModelSerializer):
    stops = RouteStopSerializer(many=True)

    class Meta:
        model = Route
        fields = ('id', 'route_name','route_start','route_end','stops')
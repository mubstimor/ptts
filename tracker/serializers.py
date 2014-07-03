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

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'route_name', 'route_start','route_end')

class RouteStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ('id', 'stop_name', 'latitude','longitude')

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buse
        fields = ('id','license_number','imeib', 'route_id')

class CordinateSerializer(serializers.ModelSerializer):
    # bus_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model =coordinate
        fields = ('id','imei', 'bus_id', 'route_id', 'latitude', 'longitude','date_added')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    # bus_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model =coordinate
        fields = ('id','bus_id', 'route_id', 'latitude', 'longitude','date_added')

class StopSerializer(serializers.ModelSerializer):
    stops = RouteStopSerializer(many=True)

    class Meta:
        model = Route
        fields = ('id', 'route_name','route_start','route_end','stops')
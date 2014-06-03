from django.contrib import admin
from tracker.models import *

# admin.site.register(coordinate)

class BusAdmin(admin.ModelAdmin):
    list_display = ('license_number','date_added', 'route')
admin.site.register(Bus, BusAdmin)

class RouteAdmin(admin.ModelAdmin):
    frontend_editable_fields = ('route_name','route_start')
    list_display = ('route_name','route_start','route_end','date_added')
admin.site.register(Route, RouteAdmin)

class Route_StopAdmin(admin.ModelAdmin):
    list_display = ('stop_name','latitude','longitude')
admin.site.register(Route_Stop, Route_StopAdmin)

class CordinateAdmin(admin.ModelAdmin):
    list_display = ('latitude','longitude', 'imei')
admin.site.register(coordinate, CordinateAdmin)
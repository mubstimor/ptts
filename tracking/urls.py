from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from tracker import views
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'view_routes', views.RouteViewSet)
router.register(r'buses', views.BusViewSet)
router.register(r'dstops', views.StopsViewSet)

urlpatterns = patterns('',
    url(r'^$', 'tracker.views.home', name='home'),
    url(r'^about', 'tracker.views.about', name='about'),
    url(r'^contact', 'tracker.views.contact', name='contact'),
    url(r'^thankyou/', 'tracker.views.thankyou'),
    url(r'^demo', 'tracker.views.demo', name='demo'),
    url(r'^benefits', 'tracker.views.benefits', name='benefits'),
    url(r'^gps', 'tracker.views.gps', name='gps'),
    url(r'^popup', 'tracker.views.route_stops_data', name='time'),
    # url(r'^find_bus', 'tracker.views.find_bus_location', name='find_bus'),

    #provides for markers
    # url(r'^find_bus', 'tracker.views.current_bus_location', name='find_bus'),

    url(r'^find_bus', 'tracker.views.find_bus', name='find_bus'),

    url(r'^routes', 'tracker.views.routes', name='routes'),
    url(r'^get_started', 'tracker.views.get_started', name='get_started'),
    url(r'^route_stops/(?P<route_id>\d+)/$', 'tracker.views.route_stops' , name='route_stops'),
    url(r'^stops/get/(?P<route_id>\d+)/$', 'tracker.views.route_stops' , name='route_stops'),
    url(r'^rstops', 'tracker.views.rstops', name='rstops'),

    url(r'^cordinates/$', 'tracker.views.cordinate_list'),

    url(r'^buses/(?P<pk>\d+)/$', 'tracker.views.bus_detail'),
    url(r'^getbus/(?P<license>.+)/$', 'tracker.views.search_bus'),

    url(r'^getbuslocations/(?P<route>.+)/$', 'tracker.views.get_currentBusLocations'),
    url(r'^getroutestops/(?P<route>.+)/$', 'tracker.views.get_stopsOnRoute'),

    # url(r'^mdata/$', 'tracker.views.RouteAndStopsData'),

    # url(r'^buses/$', views.BusList.as_view()),
    # url(r'^buses/(?P<pk>[0-9]+)/$', views.BusDetail.as_view()),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

# urlpatterns = format_suffix_patterns(urlpatterns)
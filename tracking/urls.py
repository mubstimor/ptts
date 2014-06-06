from django.conf.urls import patterns, include, url
from rest_framework import routers
from tracker import views
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'view_routes', views.RouteViewSet)

urlpatterns = patterns('',
    url(r'^$', 'tracker.views.home', name='home'),
    url(r'^about', 'tracker.views.about', name='about'),
    url(r'^contact', 'tracker.views.contact', name='contact'),
    url(r'^thankyou/', 'tracker.views.thankyou'),
    url(r'^demo', 'tracker.views.demo', name='demo'),
    url(r'^benefits', 'tracker.views.benefits', name='benefits'),
    url(r'^gps', 'tracker.views.gps', name='gps'),
    url(r'^find_bus', 'tracker.views.find_bus', name='find_bus'),
    url(r'^routes', 'tracker.views.routes', name='routes'),
    url(r'^get_started', 'tracker.views.get_started', name='get_started'),
    url(r'^route_stops/(?P<route_id>\d+)/$', 'tracker.views.route_stops' , name='route_stops'),
    url(r'^stops/get/(?P<route_id>\d+)/$', 'tracker.views.route_stops' , name='route_stops'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

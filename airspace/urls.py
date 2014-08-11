from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from radar.urls import urlpatterns as radar_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'airspace.views.home', name='home'),
                       # url(r'^airspace/', include('airspace.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^$', RedirectView.as_view(url='radar/'), name='redirect_to_radar'),
                       url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += radar_urlpatterns
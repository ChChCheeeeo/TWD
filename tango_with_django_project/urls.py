from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
	'',
    url(r'^admin/', include(admin.site.urls)),
    # www.stuff.com/rango/index
    # cut rango here, pass index to rango.urls
    url(r'^rango/', include('rango.urls', namespace='rango')),
)

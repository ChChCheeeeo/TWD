from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


urlpatterns = patterns(
	'',
    url(r'^admin/', include(admin.site.urls)),
    # www.stuff.com/rango/index
    # cut rango here, pass index to rango.urls
    url(r'^rango/', include('rango.urls', namespace='rango')),
)


# for media
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
            'serve',
            {
                'document_root': settings.MEDIA_ROOT
            }
        ),
    )
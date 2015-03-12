from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


urlpatterns = patterns(
	'',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
     # connect project urls.py to app urls.py
    # The added mapping looks for url strings that 
    # match the patterns ^rango/. When a match is 
    # made the remainder of the url string is then 
    # passed onto and handled by rango.urls (which 
    # we have already configured). This is done with 
    # the help of the include() function from within 
    # django.conf.urls. 
    # www.stuff.com/rango/index
    # cut rango here, pass index to rango.urls
    url(r'^rango/', include('rango.urls', namespace='rango')),
)


# for media
if settings.DEBUG:
    urlpatterns += patterns(
        # Pattern states that for any file 
        # requested with a URL starting with 
        # media/, the request will be passed to the 
        # django.views.static view. It handles the 
        # dispatching of uploaded media files.
        'django.views.static',
        (r'^media/(?P<path>.*)',
            'serve',
            {
                'document_root': settings.MEDIA_ROOT
            }
        ),
    )
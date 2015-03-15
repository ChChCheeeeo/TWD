from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns(
    #  When the URL pattern matching takes place, only 
    # a portion of the original URL string is 
    # considered. Django project will first process the
    # original URL string (i.e. 
    # http://www.tangowithdjango.com/rango/). Once 
    # processed, it is removed, with the remained
    # being passed for pattern matching. In 
    # this instance, there would be nothing left - so 
    # an empty string would match!
	'',
    # Any URL supplied by the user that matches this 
    # pattern means that the view views.index() would 
    # be invoked by Django. The view would be passed
    # a HttpRequest object as a parameter, containing 
    # information about the user's request to the
    # server.
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, 
    	name='add_category'),
    # pass the value of the category_name_url parameter
    # to the category() function. Invoke view.category
    # when regex is matched. Matching view then passed
    # to view view.category() as paremeter
    # category_name_slug the only argument after the 
    # mandatory request argument. make sure URL
    # pattern matches paramenters that the view takes
    # in. From below deduce that the characters (both 
    # alphanumeric and underscores) between category/ 
    # and the trailing / at the end of a matching URL 
    # are to be passed to method views.category() as 
    # named parameter category_name_slug. For example, 
    # the URL category/python-books/ would yield a 
    # category_name_slug of python-books.
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', 
    	views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', 
		views.add_page, name='add_page'),
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^register/$', views.register, name='register'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^search/', views.search, name='search'),
)
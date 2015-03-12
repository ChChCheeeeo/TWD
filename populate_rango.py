import os
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 
    'tango_with_django_project.settings'
)

# When importing Django models, make sure you have 
# imported your project's settings by importing 
# django and setting the environment variable 
# DJANGO_SETTINGS_MODULE to be the project setting 
# file. Then you can call django.setup() to import 
# the django settings. If you don't, an exception 
# will be raised. This is why we import Category and
#  Page after the settings have been loaded.

import django
django.setup()

from rango.models import Category, Page
import random
def getViewsCount():
    return random.uniform(1,100)

def populate():
    python_cat = add_cat(
        name = 'Python', 
        views = 128,
        likes = 64
    )

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/",
        views=getViewsCount()
    )

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
        views=getViewsCount()
    )

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
        views=getViewsCount()
    )

    #################################################

    django_cat = add_cat(
        name = "Django",
        views = 64,
        likes = 32
    )

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
        views=getViewsCount()
    )

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        views=getViewsCount()
    )

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
        views=getViewsCount()
    )

    #################################################

    frame_cat = add_cat(
        name = "Other Frameworks",
        views = 32,
        likes = 16
    )

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views=getViewsCount()
    )

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
        views=getViewsCount()
    )

    #################################################


    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(
            category=cat, 
            title=title)[0]

    p.url=url
    p.views=views
    p.save()
    
    return p

def add_cat(name, views=0, likes=0):
     # don't want to create duplicates of the same 
    # entry, we can use get_or_create() to check if 
    # the entry exists in the database. method returns 
    # a tuple of (object, created). The first element 
    # object is a reference to the model instance that 
    # the get_or_create() method creates if the database
    #  entry was not found. The entry is created using
    #  the parameters you pass to the method - just like 
    # category, title, url and views in the example above. 
    # If the entry already exists in the database, the 
    # method simply returns the model instance 
    # corresponding to the entry. created is a boolean 
    # value; true is returned if get_or_create() had to 
    # create a model instance. The [0] at the end 
    # of our call to the method to retrieve the 
    # object portion of the tuple returned from 
    # get_or_create(). 
    c = Category.objects.get_or_create(
        name=name,
        views=views,
        likes=likes)[0]

    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()

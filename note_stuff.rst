# BING KEY #
 i+TnawhClqnKXjZp/DGn+MhuRNK4ov/WcItiVBAnSuI

#############
When in doubt
#############
Delete db and migrations
python manage.py syncdb
python populate_rango.py
python manage.py syncdb
python manage.py makemigrations rango
python manage.py migrate



python django-admin.py startapp appname
python manage.py migrate to build initial db
Add appname to settings.py
Update project urls.py to include appname.urls.py
Create appname.views and add views
Update appname.urls to be able to find views
python manage.py runserver to tests site so far
Server may need to be restarted when views are changed.
There's a different between project-wide templates directory and app-specific templates directory. 
After createing the template, change settings.py to point to it under TEMPLATE_DIRS using absoulte value.
After setting up template path, make an index.html and plate it in the templates/rango directory and adjust the views.py file to account for this new page.
Modify templates to serve static media. Static medis is not generated dynamically.
Update settings.py so STATIC_PATH points to static media directory. 
Once static files can be found, they can be accessed via templats.
The { % static % } tag should be used whenever callilng static media in a template.
Css and javascript can also be called and used in templates.
the DEBUG variable in settings.py, lets you control the output when an error occurs, and is used for debugging. When the application is deployed it is not secure to leave DEBUG equal to True. When you set DEBUG to be False, then you will need to set the ALLOWED_HOSTS variable in settings.py, when running on your local machine this would be 127.0.0.1. You will also need to update the project urls.py file
Static media server allows to upload media.
Create media directory next to templates and static files.
Modify project urls to know where media directory is.
Modify settings.py and set MEDIA_URL and MEDIA_ROOT
Django encapsulates dbs tables through models.
Models are like python objects that describe data models/tables.
Set up required dbs and models.
Db configuration needs to be setup before creating any models.
Update DATABASES in settings.py (usally already set by defaultto use sqllite3)
Edit models.py to include models. 
create super user
python manage.py syncdb
After creating models, initialize db.
python mangage.py migrate
python mangage.py createsuperuser
use python manage.py makemigrations whenever models are changed so the changes can be registered for a particular app.
python managae.py makemigrations appname #rango
python mangage.py migrate to apply migrations
edit admin.py to include models
create populations script to fill in useful test data and populate db (called populate_rango.py and run it).
Now access data from models within views and present data in templates.
To create a data-driven webpage, make sure to seprate concerns between models, views, and templates. 
1. import models into app's view.py 
2. within views.view, query model for given data
3. pass results to template context
4. setup template to present data
5. map url to view
URL mappings could be done using unnique ids for each category or use catebory names with slugify function (to clean up spaceswitin names )
Crate new views 
Django provides user authentications. 
First set up authentications in settings.py by chaning the file at the installed apps section.
Remember, if you had to add either one of the auth or contenttypes applications to your INSTALLED_APPS tuple, you will need to resynchronise your database with the $ python manage.py syncdb command.
For every new model that you want to show up in the admin interface, make sure to register it in the admin.py file and import the UserProfile into the admin.py file. 
Remember that your database must be synchronised with the creation of a new model. Run $ python manage.py syncdb from your terminal to synchronise the new UserProfile model. This process involves Django creating one or more underlying database tables for the given model. Forgetting to synchronise your changes will result in errors explaining that the required database tables cannot be found.
The basic steps involved in creating a form and allowing users to enter data via the form is as follows.

    If you haven’t already got one, create a forms.py file within your Django application’s directory to store form-related classes.
    Create a ModelForm class for each model that you wish to represent as a form.
    Customise the forms as you desire.
    Create or update a view to handle the form - including displaying the form, saving the form data, and flagging up errors which may occur when the user enters incorrect data (or no data at all) in the form.
    Create or update a template to display the form.
    Add a urlpattern to map to the new view (if you created a new one).

Register new models in the admin.py to make it visible. 
To provide the user registration functionality we will go through the following steps:

    Create a UserForm and UserProfileForm.
    Add a view to handle the creation of a new user.
    Create a template that displays the UserForm and UserProfileForm.
    Map a URL to the view created.
    Link the index page to the register page

You should be aware of the enctype attribute for the <form> element. When you want users to upload files from a form, it’s an absolute must to set enctype to multipart/form-data.
You should also should remember to include the CSRF token, too. Ensure that you include {% csrf_token %} within your <form> element.
Next we need to handle both the rendering of the form, and the processing of form input data.
Edit urls to new views.

 Adding Login Functionality

With the ability to register accounts completed, we now need to add login in functionality. To achieve this we will need to undertake the workflow below:

    Create a login in view to handle user credentials
    Create a login template to display the login form
    Map the login view to a url
    Provide a link to login from the index page

The basic approach to using inheritance in templates is as follows.

    Identify the re-occurring parts of each page that are repeated across your application (i.e. header bar, sidebar, footer, content pane)
    In a base template, provide the skeleton structure of a standard page along with any common content (i.e. the copyright notice that goes in the footer, the logo and title that appears in the section), and then define a number of blocks which are subject to change depending on which page the user is viewing.
    Create specific templates - all of which inherit from the base template - and specify the contents of each block.

Use templates when possible and use the url tag.
Django framework used sessions and cookies to handle the login and logout functionality (all behind the scenes).

Test cookies existance with The three of particular interest to us are set_test_cookie(), test_cookie_worked() and delete_test_cookie(). In one view, you will need to set a cookie. In another, you’ll need to test that the cookie exists. Two different views are required for testing cookies because you need to wait to see if the client has accepted the cookie from the server.
In the previous example, we used client side cookies. However, a more secure way to save session information is to store any such data on the server side. We can then use the session ID cookie which is stored on the client side (but is effectively anonymous) as the key to unlock the data.
When using cookies you can use Django’s session framework to set cookies as either browser-length sessions or persistent sessions.
Run a cron job to clear cookies from time to time.

pip install django-registration-redux and update settings.py file and the project urls.py file to reference the registration package. then setup templates for the registratin package (dosn't come with their own)
Create a new directory under projects templates.as it will look in this directory for the templates it requires.
Createa a registraion form in project templates
Bootstrap if wanting and update all templates.
use temlatetags to keep sidebar browsing consitent between pages.
You will need to restart your server every time you modify the templatetags so that they are registered.
Get an API marketplace key
Wrte  search api query function.
incorpoerate jquery when possible.
include jquery references in base template
include ajax functionaly if warrented
write and run tests
django has simple tests commands
python manage.py test rango
 a database called default is referred to. When you run tests, a temporary database is constructed, which your tests can populate, and perform operations on. This way your testing is performed independently of your live database.
Django also provides testing mechanisms to test views. It does this with a mock client, that internally makes a calls a django view via the url. In the test you have access to the response (including the html) and the context dictionary.
pip install coverage
coverage run --source='.' manage.py test rango
test coverage 
deploy prjects when ready

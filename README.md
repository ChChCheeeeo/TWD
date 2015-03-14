# TWD
https://github.com/leifos/tango_with_django
https://github.com/leifos/tango_with_django_book

django-admin.py startproject tango_with_django_project

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app.

python manage.py startapp rango
update settings.py with my app names
update views.py
update urls.py to account for any new view.
update project urls.py to find app urls.py

tempaltes are dispatched vida views.
update setting.py to add path to project templates dir
create a template.html and update the view that address that tempates to use it.
When a template file is loaded with the Django templating system, a template context is created.template context is essentially a Python dictionary that maps template variable names with Python variables. 

static files are held in the static directory and update settings.py to know where the directory is
 STATIC_URL defines the URL to access media via the web server, STATICFILES_DIRS allows you to specify the location of the newly created static directory on your local disk. Static media can also be accessed through templates.

 setup a development media server. first create a media directory and update the project urls.py file to see the media dir and update settings.py as well.

Django encapsulates databases tables through models. Essentially, a model is a Python object that describes your data model/table. Instead of directly working on the database table via SQL, all you have to do is manipulate the corresponding Python object.

Configure db before telling django about models. Django uses sqlite3 by default and has default settings,to use other dbs in settings.py need to add  other keys like USER, PASSWORD, HOST and PORT can also be added to the dictionary. then add models to models.py

Django 1.7 provides a migration tool to setup and update the database to reflect changes in the models. So the process has become a little more complicated - but the idea is that if you make changes to the models, you will be able to update the database without having to delete it.

Setup Database and Create Superuser. This is done via the migrate command.

python manage.py migrate

then create a superuser to manage the database.

python manage.py createsuperuser

Whenever you make changes to the models, then you need to register the changes, via the makemigrations command for the particular app. So use

python manage.py makemigrations rango

to apply these migrations (which will essentially create the database tables), then you need to issue:

python manage.py migrate

Whenever you add to existing models, you will have to repeat this process running 
python manage.py makemigrations <app_name>
python manage.py migrate

The admin interface only contains tables relevant to the sites adminstration, Groups and Users. So we will need to instruct Django to also include the models from rango. update rango/admin.py

Add population script with test data. For example

populate_rango.py

Then run to populate db.

python populate_rango.py


When importing Django models, make sure you have imported your project’s settings by importing django and setting the environment variable DJANGO_SETTINGS_MODULE to be the project setting file. Then you can call django.setup() to import the django settings. If you don’t, an exception will be raised. This is why we import Category and Page after the settings have been loaded.

There are five main steps that you must undertake to create a data driven webpage in Django.

First, import the models you wish to use into your application’s views.py file.
Within the view you wish to use, query the model to get the data you want to present.
Pass the results from your model into the template’s context.
Setup your template to present the data to the user in whatever way you wish.
If you have not done so already, map a URL to your view.

use slugs to create clean urls.

Django comes with some neat form handling functionality, making it a pretty straightforward process to gather information from users and send it back to your web application. According to Django’s documentation on forms, the form handling functionality allows you to:

display an HTML form with automatically generated form widgets (like a text field or date picker);
check submitted data against a set of validation rules;
redisplay a form in case of validation errors; and
convert submitted form data to the relevant Python data types.

Import forms into views.py to crate a views for each form and handle theposting of form data. for example the category view.

Django’s form handling machinery processes the data returned from a user’s browser via a HTTP POST request. It not only handles the saving of form data into the chosen model, but will also automatically generate any error messages for each form field (if any are required). This means that Django will not store any submitted forms with missing information which could potentially cause problems for your database’s referential integrity. For example, supplying no value in the category name field will return an error, as the field cannot be blank.

Overriding methods implemented as part of the Django framework can provide you with an elegant way to add that extra bit of functionality for your application. There are many methods which you can safely override for your benefit, just like the clean() method in ModelForm as shown above. Check out the Official Django Documentation on Models for more examples on how you can override default functionality to slot your own in.

django.contrib.auth consists of the following aspects.

    Users.
    Permissions: a series of binary flags (e.g. yes/no) determining what a user may or may not do.
    Groups: a method of applying permissions to more than one user.
    A configurable password hashing system: a must for ensuring data security.
    Forms and view tools for logging in users, or restricting content.

edditing settings.py allow for more password hashing control

The core of Django’s authentication system is the User object, located at django.contrib.auth.models.User. A User object represents each of the people interacting with a Django application. User objects states that they are used to allow aspects of the authentication system like access restriction, registration of new user profiles and the association of creators with site content.

The model also comes with other attributes such as is_active (which determines whether a particular account is active or not).

If you would like to include other attributes than what is provided by the User model, then you will needed to create a model that is associated with the the User model. For our Rango application, we want to include two more additional attributes for each user account. Specifically, we wish to include:

    a URLField, allowing a user of Rango to specify their own website; and
    a ImageField, which allows users to specify a picture for their user profile.

  t may have been tempting to add these additional fields by inheriting from the User model directly. However, because other applications may also want access to the User model, then it not recommended to use inheritance, but instead use the one-to-one relationship.

  regiser the new UserProfile to the admin interface

Run $ python manage.py makemigrations rango from your terminal to create the migration scripts for the new UserProfile model. Then run $ python manage.py migrate

Create a view and template for UserProfile.

To provide the user registration functionality we will go through the following steps:

    Create a UserForm and UserProfileForm.
    Add a view to handle the creation of a new user.
    Create a template that displays the UserForm and UserProfileForm.
    Map a URL to the view created.
    Link the index page to the register page

add login in functionality. To achieve by

    Create a login in view to handle user credentials
    Create a login template to display the login form
    Map the login view to a url
    Provide a link to login from the index page
use decorators to restrict access to unauthorized users
To enable users to log out gracefully it would be nice to provide a logout option to users. Django comes with a handy logout() function that takes care of ensuring that the user is logged out, that their session is ended, and that if they subsequently try to access a view, it will deny them access.

The basic approach to using inheritance in templates is as follows.

    Identify the re-occurring parts of each page that are repeated across your application (i.e. header bar, sidebar, footer, content pane)
    In a base template, provide the skeleton structure of a standard page along with any common content (i.e. the copyright notice that goes in the footer, the logo and title that appears in the section), and then define a number of blocks which are subject to change depending on which page the user is viewing.
    Create specific templates - all of which inherit from the base template - and specify the contents of each block.


Now that we’ve identified our base template, we can prepare it for our inheriting templates. To do this, we need to include a Template Tag to indicate what can be overridden in the base template - this is done through the use of blocks.

Templates are very powerful and you can even create your own template tags. Here we have shown how we can minimise the repetition of structure HTML in our templates.

However, templates can also be used to minimise code within your application’s views. For example, if you wanted to include the same database-driven content on each page of your application, you could construct a template that calls a specific view to handle the repeating portion of your webpages. This then saves you from having to call the Django ORM functions which gather the required data for the template in every view that renders it.

To learn more about the extensive functionality offered by Django’s template language, check out the official Django documentation on templates.

cookies

Whenever a request to a website is made, the webserver returns the content of the requested page. In addition, one or more cookies may also be sent to the client, which are in turn stored in a persistent browser cache. When a user requests a new page from the same web server, any cookies that are matched to that server are sent with the request. The server can then interpret the cookies as part of the request’s context and generate a response to suit.

As an example, you may login to a site with a particular username and password. When you have been authenticated, a cookie may be returned to your browser containing your username, indicating that you are now logged into the site. At every request, this information is passed back to the server where your login information is used to render the appropriate page - perhaps including your username in particular places on the page. Your session cannot last forever, however - cookies have to expire at some point in time - they cannot be of infinite length. 

The passing of information in the form of cookies can open up potential security holes in your web application’s design. a majority of websites use cookies for application specific functionality.

HTTP is a stateless protocol. This therefore means that a client computer running a web browser must establish a new network connection (a TCP connection) to the server each time a resource is requested (HTTP GET) or sent (HTTP POST)

The most commonly used way of holding state is through the use of a session ID stored as a cookie on a client’s computer. A session ID can be considered as a token (a sequence of characters) to identify a unique session within a particular web application. Instead of storing all kinds of information as cookies on the client (such as usernames, names, passwords...), only the session ID is stored, which can then be mapped to a data structure on the web server. Within that data structure, you can store all of the information you require. This approach is a much more secure way to store information about users. This way, the information cannot be compromised by a insecure client or a connection which is being snooped.

To test out cookies, you can make use of some convenience methods provided by Django’s request object. The three of particular interest to us are set_test_cookie(), test_cookie_worked() and delete_test_cookie(). In one view, you will need to set a cookie. In another, you’ll need to test that the cookie exists. Two different views are required for testing cookies because you need to wait to see if the client has accepted the cookie from the server.

Session cookies accumulate. So if you are using the database backend you will have to periodically clear the database that stores the cookies. This can be done using python manage.py clearsessions. 

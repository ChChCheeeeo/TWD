=============================
Creating a new Django Project
=============================

1. To create the project run, python django-admin.py
startproject <name>, where <name> is the name of them
project you wish to create.

=================================
Creating a new Django application
=================================

1. To create a new application run, $ python manage.py startapp <appname>, where <appname> is the name of the application you wish to create.

2. Tell your Django project about the new application by adding it to the INSTALLED_APPS tuple in your project’s settings.py file.

3. In your project urls.py file, add a mapping to the application.

4. In your application’s directory, create a urls.py file to direct incoming URL strings to views.

5. In your application’s view.py, create the required views ensuring that they return a HttpResponse object.


==============
Basic Workflow
==============
With the chapter complete, you should now know how to setup and create templates, use templates within your views, setup and use Django to send static media files, include images within your templates and setup Django’s static media server to allow for file uploads. We’ve actually covered quite a lot!

Creating a template and integrating it within a Django view is a key concept for you to understand. It takes several steps, but becomes second nature to you after a few attempts.

1. First, create the template you wish to use and save it within the templates directory you specified in your project’s settings.py file. You may wish to use Django template variables (e.g. {{ variable_name }}) within your template. You’ll be able to replace these with whatever you like within the corresponding view.

2. Find or create a new view within an application’s views.py file.

3. Add your view-specific logic (if you have any) to the view. For example, this may involve extracting data from a database.

4. Within the view, construct a dictionary object which you can pass to the template engine as part of the template’s context.

5. Make use of the render() helper function to generate the rendered response. Ensure you reference the request, then the template file, followed by the context dictionary!

6. If you haven’t already done so, map the view to a URL by modifying your project’s urls.py file - and the application-specific urls.py file if you have one.

The steps involved for getting a static media file onto one of your pages is another important process you should be familiar with. Check out the steps below on how to do this.

1. Take the static media file you wish to use and place it within your project’s static directory. This is the directory you specify in your project’s STATICFILES_DIRS tuple within settings.py.

2. Add a reference to the static media file to a template. For example, an image would be inserted into an HTML page through the use of the <img /> tag.

3. Remember to use the {% load staticfiles %} and {% static "filename" %} commands within the template to access the static files.

===============
Basic Workflows
===============

Now that we’ve covered the core principles of dealing with Django’s models functionality, now is a good time to summarise the processes involved in setting everything up. We’ve split the core tasks into separate sections for you.
===============================
6.8.1. Setting up your Database
===============================

With a new Django project, you should first tell Django about the database you intend to use (i.e. configure DATABASES in settings.py). You can also register any models in the admin.py file to make them accessible via the admin interface.
6.8.2. Adding a Model

The workflow for adding models can be broken down into five steps.

1. First, create your new model(s) in your Django application’s models.py file.

2. Update admin.py to include and register your new model(s).

3. Then perform the migration $ python manage.py sqlmigrate <app_name>

4. Apply the changes $ python manage.py migrate. This will create the necessary infrastructure within the database for your new model(s).

5. Create/Edit your population script for your new model(s).

Invariably there will be times when you will have to delete your database. In which case you will have to run the migrate command, then createsuperuser command, followed by the sqlmigrate commands for each app, then you can populate the database.


=================================
Basic Workflow: Data Driven Pages
=================================

There are five main steps that you must undertake to create a data driven webpage in Django.

1. First, import the models you wish to use into your application’s views.py file.

2. Within the view you wish to use, query the model to get the data you want to present.

3. Pass the results from your model into the template’s context.

4. Setup your template to present the data to the user in whatever way you wish.

5. If you have not done so already, map a URL to your view.

These steps highlight how Django’s framework separates the concerns between models, views and templates.

=====
FORMS
=====

The basic steps involved in creating a form and allowing users to enter data via the form is as follows.

1. If you haven’t already got one, create a forms.py file within your Django application’s directory to store form-related classes.

2. Create a ModelForm class for each model that you wish to represent as a form.

3. Customise the forms as you desire.

4. Create or update a view to handle the form - including displaying the form, saving the form data, and flagging up errors which may occur when the user enters incorrect data (or no data at all) in the form.

5. Create or update a template to display the form.

6. Add a urlpattern to map to the new view (if you created a new one).

This workflow is a bit more complicated than previous workflows, and the views that we have to construct have a lot more complexity as well. However, once you undertake the process a few times it will be pretty clear how everything pieces together.

=================================
Basic Considerations and Workflow
=================================


When using cookies within your Django application, there’s a few things you should consider:

    First, consider what type of cookies your web application requires. Does the information you wish to store need to persist over a series of user browser sessions, or can it be safely disregarded upon the end of one session?
    Think carefully about the information you wish to store using cookies. Remember, storing information in cookies by their definition means that the information will be stored on client’s computers, too. This is a potentially huge security risk: you simply don’t know how compromised a user’s computer will be. Consider server-side alternatives if potentially sensitive information is involved.
    As a follow-up to the previous bullet point, remember that users may set their browser’s security settings to a high level which could potentially block your cookies. As your cookies could be blocked, your site may function incorrectly. You must cater for this scenario - you have no control over the client browser’s setup.

If client-side cookies are the right approach for you then work through the following steps:

    You must first perform a check to see if the cookie you want exists. This can be done by checking the request parameter. The request.COOKIES.has_key('<cookie_name>') function returns a boolean value indicating whether a cookie <cookie_name> exists on the client’s computer or not.
    If the cookie exists, you can then retrieve its value - again via the request parameter - with request.COOKIES[]. The COOKIES attribute is exposed as a dictionary, so pass the name of the cookie you wish to retrieve as a string between the square brackets. Remember, cookies are all returned as strings, regardless of what they contain. You must therefore be prepared to cast to the correct type.
    If the cookie doesn’t exist, or you wish to update the cookie, pass the value you wish to save to the response you generate. response.set_cookie('<cookie_name>', value) is the function you call, where two parameters are supplied: the name of the cookie, and the value you wish to set it to.

If you need more secure cookies, then use session based cookies:

    Make sure that MIDDLEWARE_CLASSES in settings.py contains ‘django.contrib.sessions.middleware.SessionMiddleware’.
    Configure your session backend SESSION_ENGINE. See the official Django Documentation on Sessions for the various backend configurations.
    Check to see if the cookie exists via requests.sessions.get()
    Update or set the cookie via the session dictionary, requests.session['<cookie_name>']

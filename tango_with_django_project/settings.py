"""
Django settings for tango_with_django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
STATIC_PATH = os.path.join(BASE_DIR,'static')
#  MEDIA_ROOT is used to tell Django where uploaded 
#files should be stored on your local disk. Here it
# gives This gives an absolute path of 
# <workspace>/tango_with_django_project/media/.
# development media server supplied with Django is 
# very useful for debugging purposes. it should not 
# be used in a production environment. read the
# docs.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# update project urls.py first
#  MEDIA_URL defines the base URL from which all 
# media files will be accessible on development 
# server. Setting the MEDIA_URL for example to 
# /media/ will mean that user uploaded files will 
# be available from the URL 
# http://127.0.0.1:8000/media/
MEDIA_URL = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# glad this isn't production.
SECRET_KEY = '+i*kg2#g%#^w0_+nr-94rb5ti0t^9$4$mjgv=mgl&f3iw$weyp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (
        # Put strings here, like 
    # "/home/html/django_templates" or 
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, 
    # not relative paths.
    TEMPLATE_PATH,
)


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # default
    'django.contrib.admin',
    # access to the authentication system
    'django.contrib.auth',
    # used by the authentication application to 
    # track models installed in your database
    'django.contrib.contenttypes',
    # store session information in a
    #  Django model/database
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party
    'registration',
    #my apps
    'rango',
)

MIDDLEWARE_CLASSES = (
    #  SessionMiddleware middleware which enables the
    # creation of unique sessionid cookies.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tango_with_django_project.urls'

WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    STATIC_PATH,
)


# want more control over how the passwords are hashed
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
)

# handle the scenario where a user attempts to
# access the restricted() view, but is not
# logged in. What do we do with the user?
# simplest approach is to redirect their browser.
# define the variable LOGIN_URL with the URL
# you'd like to redirect users to that aren't
# logged in, i.e. the login page located
# at /rango/login/:
# This ensures that the login_required() decorator
# will redirect any user not logged in to the URL
# /rango/login/
#LOGIN_URL = '/rango/login'

REGISTRATION_OPEN = True        # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/rango/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'  # The page users are directed to if they are not logged in,
                                                                # and are trying to access pages requiring authentication

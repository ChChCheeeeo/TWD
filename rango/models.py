from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# both inherite from django.db.models.Model
# The two Python classes will be the definitions for 
# models representing categories and pages.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
# For each field, you can specify the unique 
        # attribute. If set to True, only one instance
        # of a particular value in that field may exist
        # throughout the entire database model. The 
        # field name has been set to unique - thus 
        # every category name must be unique. Can also
        # specify default and null values. This is 
        # useful if you wish to use a particular 
        # field as an additional database key. 
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    # clean urls "object fields " -> "object-fields"
    slug = models.SlugField(unique=True)
# override save method, which we will call the 
    # slugify method and update the slug field with 
    # it. Note that everytime the category name 
    # changes, the slug will also change.
    # Since the save method is called for each Category,
    # the overrided save method will be executed, 
    # updating the slug field.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # test to make sure there cant be a negative
        # views/likes number
        if self.views < 0: self.views = 0
        if self.likes < 0: self.likes = 0
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
# Model metadata is "anything that's not a field",
    #  such as ordering options (ordering), database 
    # table name (db_table), or human-readable 
    # singular and plural names (verbose_name and 
    # verbose_name_plural). None are required, and 
    # adding class Meta to a model is completely 
    # optional.
    class Meta:
        # fix catetory misspeclling
		verbose_name_plural = "Categories"


class Page(models.Model):
    # field type that allows us to create a 
    # one-to-many relationship. This allows us to 
    # create a one-to-many relationship with 
    # model/table Category, which is specified as an 
    # argument to the field's constructor. be aware 
    # that Django creates an ID field for you 
    # automatically in each table relating to a model.
    # therefore not need to explicitly define a primary 
    # key for each model
    category = models.ForeignKey(Category)
# a field for storing character data 
    # (e.g. strings). Specify max_length to provide a 
    # maximum number of characters the field can store.
    title = models.CharField(max_length=128)
    # like a CharField, but designed for storing 
    # resource URLs. may specify a 
    # max_length parameter.
    url = models.URLField()
    views = models.IntegerField(default=0)

    # passing datetime.now without the parentheses, 
    # you are passing the actual function
    # which will be called each time a record is added. 
    # else all page models will start with the same time
    first_visit = models.DateTimeField(default=datetime.now, blank=True)
    last_visit = models.DateTimeField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    # extend User to  include other attributes than
    # what is provided by the User model, 
    # create a model that is associated with the the
    # User model. Here  include two more additional
    # attributes for each user account: URLField and
    # ImageField
    
    # This line is required. Links UserProfile to a
    #  User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    # blank: users do not have to supply values
    website = models.URLField(blank=True)
    picture = models.ImageField(

        # upload_to attribute. The value of this 
        # attribute is conjoined with the project's
        # MEDIA_ROOT setting to provide a path with
        # which uploaded profile images will be
        # stored. for example attribute of 
        # profile_images will result in all
        #  profile images being stored in the
        #  directory <workspace>/
        # tango_with_django_project/media/
        # profile_images/
        upload_to='profile_images', 
        blank=True
    )

    def __unicode__(self):
        return self.user.username


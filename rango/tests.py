from django.core.urlresolvers import reverse
from rango.models import Category, Page
from django.test import TestCase
import datetime
from django.utils import timezone


def add_cat(name, views, likes):
	# helper method
	c = Category.objects.get_or_create(name=name)[0]
	c.views = views
	c.likes = likes
	c.save()
	return c

# def add_page(name, views=0, likes=0, slug, first_visit, last_visit):
# 	# PageAttribute helper
# 	p = Page.objects.get_or_create()[]
# 	p.first_visit = first_visit
# 	p.last_visit = last_visit
# 	p.name = name
# 	p.views = views
# 	p.likes = likes
# 	p.slug = slug
# 	p.save()
# 	return p

class PageAttributesTest(TestCase):
	# extend Page to include two additional fields
	# last_visit and first_visit 
	# which will be of type timedate.

    # Update the model to include these two fields
    # Update the add page functionality, and the goto functionality.
    # Add in a test to ensure the last visit or first visit is not in the future
    # Add in a test to ensure that the last visit equal to or after the first visit.
	
	# class Page(models.Model):
	#     category = models.ForeignKey(Category)
	#     title = models.CharField(max_length=128)
	#     url = models.URLField()
	#     views = models.IntegerField(default=0)
	#     first_visit = models.DateTimeField(default=datetime.now, blank=True)
	#     last_visit = models.DateTimeField(default=datetime.now, blank=True)

    def test_last_view_and_first_view_exist(self):
    	"""
    		check that last view and first view exists
    	"""
    	# TODO: find out why this doesn't work <UTC>
    	# first = timezone.now() + datetime.timedelta(days=-30)
    	# last = timezone.now()

    	first = datetime.date.today()
    	last = datetime.date.today()

    	cat = Category(name='test',views=0, likes=0)
    	cat.save()
    	p = Page(
	    		category=cat, 
	    		title='testign-assertEqual',
	    		url='http://www.google.com',
	    		views=0, 
	    		first_visit=first, 
	    		last_visit=last
    		)
    	p.save()

    	self.assertEqual(p.first_visit, first, True)
    	self.assertEqual(p.last_visit, last, True)

    def test_last_view_comes_after_first_view(self):
    	"""
    		check proper chronolocial order
    	"""
    	first = datetime.date(2014, 12, 5)
    	last = datetime.date(2014, 12, 6)

    	cat = Category(name='test',views=0, likes=0)
    	cat.save()
    	p = Page(
	    		category=cat, 
	    		title='testign-assertEqual',
	    		url='http://www.google.com',
	    		views=0, 
	    		first_visit=first, 
	    		last_visit=last
    		)
    	p.save()

    	self.assertEqual((p.first_visit <= p.last_visit), True)
    	self.assertEqual((p.last_visit >= p.first_visit), True)
    	


    def test_last_view_and_first_view_are_not_in_the_furture(self):
    	"""
    		No dates can come before "now"
    	"""
    	first = datetime.date(2014, 12, 5)
    	last = datetime.date(2014, 12, 6)
    	future = datetime.date(2014, 12, 12)

    	cat = Category(name='test',views=0, likes=0)
    	cat.save()
    	p = Page(
	    		category=cat, 
	    		title='testign-assertEqual',
	    		url='http://www.google.com',
	    		views=0, 
	    		first_visit=first, 
	    		last_visit=last
    		)
    	p.save()

    	self.assertEqual((future <= p.first_visit), False)
    	self.assertEqual((future <= p.last_visit), False)
    	
    	
	    
# class CategoryMethodTests(TestCase):
	# tests that focus on ensuring the integrity of the data housed in models. 
# 	# run with
# 	# python manage.py test rango
# 	# there are various types of assertions
# 	# look them up

# 	# Test cases inherit from TestCase
# 	# test methods start with 
# 	# test_TEST_NAME
# 	# All have assertions (which are the tests)
# 	def test_ensure_views_are_positive(self):
# 		"""
# 			ensure_views_are_positive should results 
# 			True for categories where views are zero or positive
# 		"""
# 		cat = Category(name='test',views=-1, likes=0)
# 		cat.save()
# 		self.assertEqual((cat.views >= 0), True)

# 	def test_slug_line_creation(self):
# 		"""
# 			slug_line_creation checks to make sure that when we add a category
# 			 an appropriate slug line is created
# 			i.e. "Random Category String" -> "random-category-string"
# 		"""

# 		# this examlpe, Category needs named positional else get annoying error
# 		cat = Category(name='Random Category String')#, views=0, likes=0)
# 		cat.save()
# 		self.assertEqual(cat.slug, 'random-category-string')



class IndexViewTests(TestCase):
	pass
	# for views, use a mock client. it internally calls django views 
	# via the url. In the test you have access to the response 
	# (including the html) and the context dictionary.

	#test that checks that when the index page loads, 
	# it displays the message that There are no categories present, 
	# when the Category model is empty.
	# def test_index_view_with_no_categories(self):
	# 	"""
	# 		If no questions exist, an appropriate message should be displayed.
	# 	"""
	# 	# calling index without pass it a context dictionary
	# 	# thus not categories variable.
	# 	# TestCase has client object which can make 
	# 	# requests
	# 	response = self.client.get(reverse('index'))
	# 	self.assertEqual(response.status_code, 200) # did page load ok
	# 	self.assertContains(response, "There are no categories present.") # does response have proper response
	# 	self.assertQuerysetEqual(response.context['categories'], []) # does context_dictionary contain empty list

	# def test_index_view_with_categories(self):
	# 	"""
	# 		If no questions exist, an appropriate 
	# 		message should be displayed.
	# 	"""

	# 	add_cat('test',1,1)
	# 	add_cat('temp',1,1)
	# 	add_cat('tmp',1,1)
	# 	add_cat('tmp test temp',1,1)

	# 	response = self.client.get(reverse('index'))
	# 	self.assertEqual(response.status_code, 200) # does it load
	# 	self.assertContains(response, "tmp test temp") # does it contain 

	# 	num_cats =len(response.context['categories'])
	# 	self.assertEqual(num_cats , 4) #did the right number of cats appear
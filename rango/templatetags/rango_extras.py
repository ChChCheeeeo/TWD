from rango.models import Category
from django import template

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
	# turn this into a template tag by loading it
	# where you want to use it and call the method
	# e.g.
	# { % load rango_extras % }
	# { % get_category_list % }
	# cat=None and
	# 'act_cat': cat is to paramertize
	# get_category_list 
	# pass category to template
    return {'cats': Category.objects.all(), 'act_cat': cat}

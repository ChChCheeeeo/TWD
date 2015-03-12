from rango.models import Category, Page, UserProfile
from django.contrib import admin


# In the admin interface you may want it to 
# automatically pre-populate the slug field as your 
# type in the category name.
class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
    	'slug':('name',)
    }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

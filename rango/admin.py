from rango.models import Category, Page
from django.contrib import admin


class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
    	'slug':('name',)
    }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
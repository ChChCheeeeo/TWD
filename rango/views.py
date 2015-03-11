from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

def about(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {
        'categories': category_list
    }

    return render(request, 'rango/index.html', context_dict)



def index(request):
	context_dict = {
		'boldmessage': "I am bold font from the context"
	}
	return render(request, 'rango/index.html', context_dict)


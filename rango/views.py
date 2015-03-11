from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    context_dict = {
    	'boldmessage': "You've reached the about page",
    }

    return render(
        request,
        'rango/about.html',
        context_dict
    )
	


def index(request):
	context_dict = {
		'boldmessage': "I am bold font from the context"
	}
	return render(request, 'rango/index.html', context_dict)


from django.shortcuts import render
from django.http import HttpResponse

def about(request):
	context = """
		Rango says here is the about page.
		<br/> 
		<a href='/rango/'>
			Index
		</a>
	"""
	return HttpResponse(context)


def index(request):
	context_dict = {
		'boldmessage': "I am bold font from the context"
	}
	return render(request, 'rango/index.html', context_dict)


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
	context = """
		Rango says: Hello world! 
		<br/> 
		<a href='/rango/about'>
			About
		</a>
	"""
	return HttpResponse(context)

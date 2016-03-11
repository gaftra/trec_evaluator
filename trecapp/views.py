from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

	context_dict = {'boldmessage': "Use google"}
	
	return render(request, 'trecapp/index.html', context_dict)
	
def about(request):
	return render(request, 'trecapp/about.html')

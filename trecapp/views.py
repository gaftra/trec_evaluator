from django.shortcuts import render
from django.http import HttpResponse
from trecapp.models import Track

# Create your views here.
def index(request):

	# Gets a list of all the current Tracks
	track_list = Track.objects.order_by('title')
	context_dict = {'tracks': track_list}
	
	return render(request, 'trecapp/index.html', context_dict)
	
def about(request):
	return render(request, 'trecapp/about.html')

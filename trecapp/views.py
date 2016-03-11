from django.shortcuts import render
from django.http import HttpResponse
from trecapp.models import Track
from trecapp.models import Task

# Create your views here.
def track(request, track_name_slug):
	context_dict = {}
	
	try:
		track = Track.objects.get(slug=track_name_slug)
		context_dict['track_title'] = track.title
		
		tasks = Task.objects.filter(track=track)
		
		context_dict['tasks'] = tasks
		context_dict['track'] = track
	except Track.DoesNotExist:
		pass
		
	return render(request, 'trecapp/track.html', context_dict)

def index(request):
	# Gets a list of all the current Tracks
	track_list = Track.objects.order_by('title')
	context_dict = {'tracks': track_list}
	
	return render(request, 'trecapp/index.html', context_dict)
	
def about(request):
	return render(request, 'trecapp/about.html')

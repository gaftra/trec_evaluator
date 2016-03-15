from django.shortcuts import render
from django.http import HttpResponse
from trecapp.models import Track
from trecapp.models import Task
from trecapp.models import Researcher
from trecapp.models import Run
from trecapp.forms import UploadRunForm

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
	
def task(request, track_name_slug, task_name_slug):
	context_dict = {}
	
	try:
		track_name = Track.objects.get(slug=track_name_slug)
		task = Task.objects.get(slug=task_name_slug, track=track_name)
		track = Track.objects.get(slug=track_name_slug)
		researcher = Researcher.objects.get(username="jill") #temporary, swiwch to user logged in later
		context_dict['track'] = track
		context_dict['task_title'] = task.title
		context_dict['task'] = task
		
		# Upload Run Form
				
		if request.method == "POST":
			form = UploadRunForm(request.POST, request.FILES)
			
			if form.is_valid():
				run = form.save(commit=False)
				run.researcher = researcher
				run.task = task
				form.save(commit=True)
					
				#return task(request, track_name_slug, task_name_slug)
				return index(request)
				
			else:
				print "YOUR FORM ISN'T FUCKEN VALID"
				print form.errors
			
		else:
			form = UploadRunForm()
		
		context_dict['form'] = form
		context_dict['researcher'] = researcher
		
	except Task.DoesNotExist:
		pass
		
	return render(request, 'trecapp/task.html', context_dict)

def index(request):
	# Gets a list of all the current Tracks
	track_list = Track.objects.order_by('title')
	context_dict = {'tracks': track_list}
	
	return render(request, 'trecapp/index.html', context_dict)
	
def about(request):
	return render(request, 'trecapp/about.html')	
	
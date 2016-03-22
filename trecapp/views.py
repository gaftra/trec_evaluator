from django.shortcuts import render
from django.http import HttpResponse
from trecapp.models import Track
from trecapp.models import Task
from trecapp.models import Researcher
from django.contrib.auth.models import User
from trecapp.models import Run
from trecapp.forms import UploadRunForm, UserForm, ResearcherForm, UserEditForm
import os
from django.conf import settings
from django.core.files import File
import subprocess
from subprocess import check_output

# The view for a profile page
def profile(request):
	context_dict = {}
	
	try:
		username = User.objects.get(username=request.user.username)
		email = User.objects.get(username=request.user).email
		profile_picture = Researcher.objects.get(user=username).profile_picture
		website = Researcher.objects.get(user=username).website
		display_name = Researcher.objects.get(user=username).display_name
		organization = Researcher.objects.get(user=username).organization

		context_dict['username'] = username
		context_dict['email'] = email
		context_dict['website'] = website
		context_dict['profile_picture'] = profile_picture
		context_dict['display_name'] = display_name
		context_dict['organization'] = organization
	except User.DoesNotExist:
		pass

	return render(request, 'trecapp/profile.html', context_dict)

# The view for editing a profile page
def editprofile(request):
	context_dict = {}

	#on save
	if request.method == 'POST':

		user_form = UserEditForm(data=request.POST)
		researcher_form = ResearcherForm(request.POST, request.FILES)
		
		if user_form.is_valid() and researcher_form.is_valid():
			user = User.objects.get(username=request.user)
			researcher = Researcher.objects.get(user=user)
			researcher.user = user

			user.email = request.POST.get('email')
			if 'profile_picture' in request.FILES:
				researcher.profile_picture = request.FILES.get('profile_picture')
			researcher.website = request.POST.get('website')
			researcher.display_name = request.POST.get('display_name')
			researcher.organization = request.POST.get('organization')

			user.save()
			researcher.save()

		return profile(request)
	
	#edit form	
	else:
		user_form = UserForm()
		researcher_form = ResearcherForm()

		if request.user.is_authenticated():
			try:
				username = User.objects.get(username=request.user.username)
				email = User.objects.get(username=request.user).email
				profile_picture = Researcher.objects.get(user=username).profile_picture
				website = Researcher.objects.get(user=username).website
				display_name = Researcher.objects.get(user=username).display_name
				organization = Researcher.objects.get(user=username).organization

				context_dict['username'] = username
				context_dict['email'] = email
				context_dict['website'] = website
				context_dict['profile_picture'] = profile_picture
				context_dict['display_name'] = display_name
				context_dict['organization'] = organization
			except User.DoesNotExist:
				pass

	return render(request, 'trecapp/editprofile.html', context_dict )

# The view for each track page
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
	
# The view for each task page
def task(request, track_name_slug, task_name_slug):
	context_dict = {}
	try:
		track_name = Track.objects.get(slug=track_name_slug)
		task = Task.objects.get(slug=task_name_slug, track=track_name)
		data = Run.objects.filter(task_id= task.id).order_by('-map')
		context_dict['data'] = data
	except Task.DoesNotExist:
			pass

	
	# If the user is logged in, create a form to upload a run
	if request.user.is_authenticated():
		try:
			track_name = Track.objects.get(slug=track_name_slug)
			task = Task.objects.get(slug=task_name_slug, track=track_name)
			track = Track.objects.get(slug=track_name_slug)
			user = User.objects.get(username=request.user)
			researcher = Researcher.objects.get(user=user)
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
	
					'''
					Here we interact with trec_eval to get map p10 and p20
					'''
					# Get the location of the given judgement file
					judgement_file_location = File(run.task.judgementFile).name
					judgement_file_location = judgement_file_location[1:]
					true_judgement_file_location = os.path.join(settings.BASE_DIR, judgement_file_location)

					# Get the location of the given results file
					result_file_location = File(run.result_file).name
					true_result_file_location = os.path.join(settings.MEDIA_ROOT, result_file_location)

					# Get the location of trec_eval
					trec_eval_location = os.path.join(settings.BASE_DIR, 'trec_eval')

					# Call the appropriate command, and store its results
					return_string = check_output([trec_eval_location, true_judgement_file_location, true_result_file_location])
	
					map_string = ""
					p10_string = ""
					p20_string = ""
					# Scan through returned string to extract MAP, P10 and P20
					for line in iter(return_string.splitlines()):
						if 'map' in line and not 'gm_map' in line:
							map_string = line
						if 'P_10' in line and not 'P_100' in line and not 'P_1000' in line:
							p10_string = line
						if 'P_20' in line and not 'P_200' in line:
							p20_string = line	

					# Get the values from the strings
					map_value = map_string.split()[2]
					p10_value = p10_string.split()[2]
					p20_value = p20_string.split()[2]
										

					run.map = map_value
					run.p10 = p10_value
					run.p20 = p20_value
					
					form.save(commit=True)
					
					return index(request)
					
				else:
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
	

def register(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		researcher_form = ResearcherForm(request.POST, request.FILES)
		
		if user_form.is_valid() and researcher_form.is_valid():
			user = user_form.save()
			
			user.set_password(user.password)
			user.save()
			
			researcher = researcher_form.save(commit=False)
			researcher.user = user
			
			researcher.save()
			
			registered = True
		
		else:
			print user_form.errors, researcher_form.errors
			
	else:
		user_form = UserForm()
		researcher_form = ResearcherForm()
		
	return render(request, 'trecapp/register.html', {'user_form': user_form, 'researcher_form': researcher_form, 'registered': registered } )

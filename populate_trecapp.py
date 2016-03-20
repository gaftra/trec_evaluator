# Population Script
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trec_evaluator.settings')

import django
django.setup()

from trecapp.models import Track, Task, Researcher, Run
from django.contrib.auth.models import User

# Populate the database with good data, based on github.com/leifos/wad/..../trec
def populate():
	# Create the tracks
	robust2004 = add_track(
		title="Robust2004",
		url="http://trec.nist.gov/data/t13_robust.html",
		description="News Retrieval",
		genre="News"
	)
	
	robust2005 = add_track(
		title="Robust2005",
		url="http://trec.nist.gov/data/t14_robust.html",
		description="News Retrieval",
		genre="News"
	)
	
	millionQuery = add_track(
		title="MillionQuery",
		url="http://ciir.csumass.edu/research/million/",
		description="Million Query Track",
		genre="Web"
	)
	
	terabyte = add_track(
		title="Terabyte",
		url="http://www-nlpir.nist.gov/projects/terabyte/",
		description="Terabyte Web Track",
		genre="Web"
	)
	
	apnews = add_track(
		title="APNews",
		url="",
		description="News Retrieval Track",
		genre="News"
	)
	
	# Create the tasks
	add_task(
		track = robust2005,
		title = "Ad Hoc Topic Retrieval",
		url = "http://trec.nist.gov/data/t14_robust.html",
		description = "For each topic find all the relevant documents",
		year = 2005,
		judgementFile = "/media/data/robust/aq.trec2005.qrels"
	)
	
	add_task (
		track = terabyte,
		title = "Ad Hoc Topic Retrieval",
		url = "http://www-nlpir.nist.gov/projects/terabyte/",
		description = "Find all the relevant web pages",
		year = 2005,
		judgementFile = "/media/data/web/dg.trec.qrels"
	)
	
	add_task (
		track = apnews,
		title = "Ad Hoc Topic Retrieval",
		url = "",
		description = "Find all the relevant news articles",
		year = 2001,
		judgementFile = "/media/data/news/ap.trec.qrels"
	)
	
	# Create example data researchers
	asu = add_researcher (
		username = "ASU",
		password = "ASU",
		display_name = "Alpha Team",
		organization = "AS University"
	)
	
	ck = add_researcher (
		username = "CK",
		password = "CK",
		display_name = "Chaos and Kontrol",
		organization = "CK University",
	)
	
	hk = add_researcher (
		username = "HK",
		password = "HK",
		display_name = "HongKongIR",
		organization = "HK University",
	)
	
	ict = add_researcher (
		username = "ICT",
		password = "ICT",
		display_name = "ICTer",
		organization = "University of ICT",
	)
	
	rim = add_researcher (
		username = "RIM",
		password = "RIM",
		display_name = "IRJobs",
		organization = "Royal Institute of Mayhem",
	)
	
	#Create all of leifs required test users
	jill = add_researcher(
		username = "jill",
		password = "jill",
		display_name = "jill",
		organization = "test_users",
	)
	
	jim = add_researcher (
		username = "jim",
		password = "jim",
		display_name = "jim",
		organization = "test_users",
	)
	
	joe = add_researcher (
		username = "joe",
		password = "joe",
		display_name = "joe",
		organization = "test_users",
	)
	
	bob = add_researcher (
		username = "bob",
		password = "bob",
		display_name = "bob",
		organization = "test_users"
	)
	
	jen = add_researcher (
		username = "jen",
		password = "jen",
		display_name = "jen",
		organization = "test_users",
	)
	
# Adds a track
def add_track(title, url, description, genre):
	track = Track.objects.get_or_create(title=title)[0]
	track.track_url = url
	track.description = description
	track.genre = genre
	track.save()
	return track
	
# Adds a task
def add_task(track, title, url, description, year, judgementFile):
	task = Task.objects.get_or_create(track=track, title=title)[0]
	task.task_url = url
	task.description = description
	task.year = year
	task.judgementFile = judgementFile
	task.save()
	
# Adds a researcher
def add_researcher(username, password, display_name, organization):
	user 					= User.objects.get_or_create(username=username)[0]
	# you have to use the setter so that the password isn't set in plain text but it uses the hasher.
	user.set_password(password)
	#don't forget to save it, :)
	user.save()
	researcher 				= Researcher.objects.get_or_create(user=user)[0]
	researcher.display_name = display_name
	researcher.organization = organization
	researcher.save()
	return researcher
	
# Adds a run
#def add_run():
	#stuff

if __name__ == '__main__':
	print "Starting trecapp population script..."
	populate()
	python manage.py loaddata researcher.json
	python manage.py loaddata task.json
	python manage.py loaddata track.json
	python manage.py loaddata run.json
	python manage.py loaddata leaderboard.json
	print "Done"

# Population Script
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trec_evaluator.settings')
from subprocess import call

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
	robust_adhoc = add_task(
		track = robust2005,
		title = "Ad Hoc Topic Retrieval",
		url = "http://trec.nist.gov/data/t14_robust.html",
		description = "For each topic find all the relevant documents",
		year = 2005,
		judgementFile = "/media/data/robust/aq.trec2005.qrels"
	)
	
	terabyte_adhoc = add_task (
		track = terabyte,
		title = "Ad Hoc Topic Retrieval",
		url = "http://www-nlpir.nist.gov/projects/terabyte/",
		description = "Find all the relevant web pages",
		year = 2005,
		judgementFile = "/media/data/web/dg.trec.qrels"
	)
	
	apnews_adhoc = add_task (
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

	# populate robust_adhoc with the 4 provided sample runs, all by user jill
	add_run (
		researcher = jill,
		task = robust_adhoc,
		name = "jill bm25.0.50",
		description = "Sample run using file aq.trec.bm25.0.50",
		result_file = '',
		run_type = 0,
		query_type = 0,
		feedback_type = 0,
		map = 0.1764,
		p10 = 0.3469,
		p20 = 0.3367,
	)

	add_run (
		researcher = jill,
		task = robust_adhoc,
		name = "jill bm25.0.70",
		description = "Sample run using file aq.trec.bm25.0.70.res",
		result_file = '',
		run_type = 0,
		query_type = 0,
		feedback_type = 0,
		map = 0.1619,
		p10 = 0.3163,
		p20 = 0.3061,
	)	

	add_run (
		researcher = jill,
		task = robust_adhoc,
		name = "jill pl2.2.00",
		description = "Sample run using file aq.trec.pl2.2.00.res",
		result_file = '',
		run_type = 0,
		query_type = 0,
		feedback_type = 0,
		map = 0.1692,
		p10 = 0.3306,
		p20 = 0.3092,
	)	

	add_run (
		researcher = jill,
		task = robust_adhoc,
		name = "jill pl2.5.00",
		description = "Sample run using file aq.trec.pl2.5.00.res",
		result_file = '',
		run_type = 0,
		query_type = 0,
		feedback_type = 0,
		map = 0.1771,
		p10 = 0.3735,
		p20 = 0.3378,
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
	return task
	
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
def add_run(researcher, task, name, description, result_file, run_type, query_type, feedback_type, map, p10, p20):
	researcher = researcher
	task = task
	run = Run.objects.get_or_create(researcher=researcher, task=task, name=name)[0]
	run.description = description
	run.result_file = result_file
	run.run_type = run_type
	run.query_type = query_type
	run.feedback_type = feedback_type
	run.map = map
	run.p10 = p10
	run.p20 = p20	
	run.save()
	return run

if __name__ == '__main__':
	print "Starting trecapp population script..."
	populate()
	print "Done"

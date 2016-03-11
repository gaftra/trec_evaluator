# Population Script
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trec_evaluator.settings')

import django
django.setup()

from trecapp.models import Track, Task

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
	
if __name__ == '__main__':
	print "Starting trecapp population script..."
	populate()
	print "Done"
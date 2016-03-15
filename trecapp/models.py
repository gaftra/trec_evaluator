from django.db import models
import os
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.

# STUB to get the run model working
class Researcher(models.Model):
	username = models.CharField(max_length=128, unique=True, null=False)
	password = models.CharField(max_length=128, null=False)
	
class Track(models.Model):
	title = models.CharField(max_length=128, unique=True, null=False)
	track_url = models.URLField()
	description = models.CharField(max_length=400)
	genre = models.CharField(max_length=128)
	slug = models.SlugField()
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Track, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.title
		
class Task(models.Model):
	track = models.ForeignKey(Track, null=False)
	title = models.CharField(max_length=128, null=False)
	task_url = models.URLField()
	description = models.CharField(max_length=400)
	year = models.IntegerField(default=2016)
	judgementFile = models.FileField(upload_to='/media/data', null=False)
	slug = models.SlugField()
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Task, self).save(*args, **kwargs)
		
	def __unicode__(self):
		return self.title
		
class Run(models.Model):
	#Defining enum types
	AUTOMATIC = 0
	MANUAL = 1
	RUN_TYPE = (
		(AUTOMATIC, 'Automatic'),
		(MANUAL, 'Manual'),
	)
	
	TITLE = 0
	TITLE_DESC = 1
	DESCRIPTION = 2
	ALL = 3
	OTHER = 4
	QUERY_TYPE = (
		(TITLE, "Title"),
		(TITLE_DESC, "Title + Description"),
		(DESCRIPTION, "Description"),
		(ALL, "All"),
		(OTHER, "Other"),
	)
	
	NONE = 0
	PSEUDO = 1
	RELEVANCE = 2
	FEEDBACK_OTHER = 3
	FEEDBACK_TYPE = (
		(NONE, "None"),
		(PSEUDO, "Pseudo"),
		(RELEVANCE, "Relevance"),
		(FEEDBACK_OTHER, "Other"),
	)
	
	researcher = models.ForeignKey(Researcher, null=False)
	task = models.ForeignKey(Task, null=False)
	name = models.CharField(max_length=128)
	description = models.CharField(max_length=512)
	result_file = models.FileField(upload_to='/media/results', null=False)
	run_type = models.IntegerField(choices=RUN_TYPE, default=0)
	query_type = models.IntegerField(choices=QUERY_TYPE, default=4)
	feedback_type = models.IntegerField(choices=FEEDBACK_TYPE, default=0)
	map = models.FloatField()
	p10 = models.FloatField()
	p20 = models.FloatField()
	
	def __unicode__(self):
		return self.name

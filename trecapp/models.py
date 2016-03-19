from django.db import models
import os
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

# STUB to get the run model working

def upload_dir(instance, filename):
    return 'images/' + str(instance.user.username) + '/' + filename

class Researcher(models.Model):
	# Links a researcher to a User Model Instance
	user = models.OneToOneField(User)

	# Additional attributes
	profile_picture = models.ImageField(upload_to=upload_dir, default='profile_pic.png')
	website = models.CharField(max_length=512, blank=True)
	display_name = models.CharField(max_length=30, blank=True)
	organization = models.CharField(max_length=512, blank=True)
	


	def __unicode__(self):
		return self.user.username
	
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
	
	researcher 		= models.ForeignKey(Researcher, null=False)
	task 			= models.ForeignKey(Task, null=False)
	name 			= models.CharField(max_length=128, default="")
	description		= models.CharField(max_length=512, default="")
	result_file 	= models.FileField(upload_to='results/', null=False)
	run_type 		= models.IntegerField(choices=RUN_TYPE, default=0)
	query_type 		= models.IntegerField(choices=QUERY_TYPE, default=4)
	feedback_type 	= models.IntegerField(choices=FEEDBACK_TYPE, default=0)
	map 			= models.FloatField(default=0.0, null=True)
	p10 			= models.FloatField(default=0.0, null=True)
	p20 			= models.FloatField(default=0.0, null=True)
	
	def save(self, *args, **kwargs):
		super(Run, self).save(*args, **kwargs)
		
	def __unicode__(self):
		return self.name

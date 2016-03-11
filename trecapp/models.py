from django.db import models
import os
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.
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

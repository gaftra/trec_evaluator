from django.db import models

# Create your models here.
class Track(models.Model):
	title = models.CharField(max_length=128, unique=True, null=False)
	description = models.CharField(max_length=400)
	genre = models.CharField(max_length=128)
	# TODO gonna need a url field here, probably with slugs
	
	def __unicode__(self):
		return self.title
		
class Task(models.Model):
	track = models.ForeignKey(Track, null=False)
	title = models.CharField(max_length=128, unique=True, null=False)
	description = models.CharField(max_length=400)
	year = models.IntegerField(default=2016)
	judgementFile = models.FileField(upload_to='Relevance Judgement Files/', null=False)
	# TODO gonna need a url field here, probably with slugs

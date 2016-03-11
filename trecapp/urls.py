from django.conf.urls import patterns, url
from trecapp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^track/(?P<track_name_slug>[\w\-]+)$', views.track, name='track'),
	)
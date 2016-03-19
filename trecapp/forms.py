from django import forms
from django.contrib.auth.models import User
from trecapp.models import Run, Researcher
from django.forms import ModelForm

class UploadRunForm(forms.ModelForm):
	name 			= forms.CharField(max_length=128, help_text="Please enter the runs name: ")
	description 	= forms.CharField(widget=forms.TextInput(), max_length=512, help_text="Please enter the runs description: ")
	result_file 	= forms.FileField(help_text="Select your .res file: ")
	run_type 		= forms.ChoiceField(choices=Run.RUN_TYPE, help_text="Run Type: ")
	query_type 		= forms.ChoiceField(choices=Run.QUERY_TYPE, help_text="Query Type: ")
	feedback_type	= forms.ChoiceField(choices=Run.FEEDBACK_TYPE, help_text="Feedback Type: ")
	# The following are hidden, as they will be automatically filled by trec_eval
	map = forms.FloatField(widget=forms.HiddenInput(), required=False)
	p10 = forms.FloatField(widget=forms.HiddenInput(), required=False)
	p20 = forms.FloatField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = Run
		# Hide the researcher and Task foreign keys
		exclude = ('researcher', 'task',)
		
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class ResearcherForm(forms.ModelForm):
	class Meta:
		model = Researcher
		fields = ('profile_picture', 'website', 'display_name', 'organization')
	
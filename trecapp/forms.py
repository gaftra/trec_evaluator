from django import forms
from trecapp.models import Run

class UploadRunForm(forms.Form):
	name = forms.CharField(max_length=128, help_text="Please enter the runs name: ")
	description = forms.CharField(max_length=512, help_text="Please enter the runs description: ")
	result_file = forms.FileField(help_text="Select your .res file: ")
	run_type = forms.ChoiceField(choices=Run.RUN_TYPE, help_text="Run Type: ")
	query_type = forms.ChoiceField(choices=Run.QUERY_TYPE, help_text="Query Type: ")
	feedback_type = forms.ChoiceField(choices=Run.FEEDBACK_TYPE, help_text="Feedback Type: ")
	# The following are hidden, as they will be automatically filled by trec_eval
	map = forms.FloatField(widget=forms.HiddenInput())
	p10 = forms.FloatField(widget=forms.HiddenInput())
	p20 = forms.FloatField(widget=forms.HiddenInput())
	
	class Meta:
		model = Run
		# Hide the researcher and Task foreign keys
		exclude = ('researcher', 'task')
	
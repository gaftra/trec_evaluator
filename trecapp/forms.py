from django import forms
from trecapp.models import Run

class UploadRunForm(forms.Form):
	name = forms.CharField(max_length=128, help_text="Please enter the run's name.")
	description = forms.CharField(max_length=512, help_text="Please enter the run's description.")
	result_file = forms.FileField()
	run_type = forms.ChoiceField()
	query_type = forms.ChoiceField()
	feedback_type = forms.ChoiceField()
	# The following are hidden, as they will be automatically filled by trec_eval
	map = forms.FloatField(widget=forms.HiddenInput())
	p10 = forms.FloatField(widget=forms.HiddenInput())
	p20 = forms.FloatField(widget=forms.HiddenInput())
	
	class Meta:
		model = Run
		# Hide the researcher and Task foreign keys
		exclude = ('researcher', 'task')
	
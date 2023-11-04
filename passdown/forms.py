from django import forms
from .models import PassDown, Entry
from django.forms import ModelChoiceField

class PassDownForm(forms.ModelForm):
	class Meta:
		model = PassDown
		fields = (
			'shift',
			'notes',
		)

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = (
			'modex',
			'discrepancy',
			'text_body',
			'passdown',
			'job_status',
			'cdi',
		)
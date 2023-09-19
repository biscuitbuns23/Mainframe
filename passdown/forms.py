from django import forms
from .models import PassDown, Entry

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
		fields = "__all__"

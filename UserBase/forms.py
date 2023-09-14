from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username",)
		field_classes = {'username': UsernameField}

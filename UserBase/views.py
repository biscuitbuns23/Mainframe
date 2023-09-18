from django.shortcuts import render
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import (
    CreateView, ListView, DetailView, TemplateView, UpdateView,
    DeleteView)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.mixins import LoginRequiredMixin
#from agents.mixins import OrganizerAndLoginRequiredMixin
from .forms import CustomUserCreationForm
from django.urls.base import reverse_lazy

class LandingView(TemplateView):
    template_name = "landing.html"

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")
    
class PasswordResetViewCustom(PasswordResetView):
        success_url = reverse_lazy("PasswordResetDoneView")


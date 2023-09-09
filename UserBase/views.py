from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, TemplateView, UpdateView,
    DeleteView)

class LandingView(TemplateView):
    template_name = "landing.html"
from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, TemplateView, UpdateView,
    DeleteView, FormView)


class KairosLanding(TemplateView):
    template_name = 'kairos/kairos_landing3.html'

class CreateAccount(TemplateView):
    template_name = 'kairos/create-account.html'

class WMFormsView(TemplateView):
    template_name = 'kairos/forms.html'

class CardsView(TemplateView):
    template_name = 'kairos/cards.html'

class ChartsView(TemplateView):
    template_name = 'kairos/charts.html'
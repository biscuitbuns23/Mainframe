from django.shortcuts import render
from typing import Any, Dict
from django.db.models.query import QuerySet
from .models import Entry, PassDown
from .forms import PassDownForm, EntryForm
from django.urls import reverse
from django.views.generic import (
    CreateView, ListView, DetailView, TemplateView, UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin


class EntryCreateView(LoginRequiredMixin, CreateView):
    template_name = "passdown/entry_create.html"
    form_class = EntryForm

    def get_success_url(self):
        return reverse("passdown:entry-create")

class PassDownCreateView(LoginRequiredMixin, CreateView):
    template_name = "passdown/passdown_create.html"
    form_class = PassDownForm

    def form_valid(self, form):
        entered = form.save(commit=False)
        entered.entered_by = self.request.user
        entered.save()
        return super(PassDownCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse("passdown:entry-create")

class EntryByPassdown(LoginRequiredMixin, ListView):
    template_name = "passdown/entry_by_passdown.html"
    context_object_name = "entries"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['queryset1'] = Entry.objects.filter(passdown_id=1)
        context_data['queryset2'] = PassDown.objects.filter(id=1)
        return context_data

    def get_queryset(self):
        myset = {
            "queryset1": Entry.objects.filter(passdown_id=1),
            "queryset2": PassDown.objects.filter(id=1)
        }
        return myset

class EntryListView(LoginRequiredMixin, ListView):
    template_name = "passdown/entry_list.html"
    context_object_name = "entries"

    def get_queryset(self):
        QuerySet = Entry.objects.all()
        return QuerySet

class DashboardView(TemplateView):
    template_name = 'passdown/dashboard.html'
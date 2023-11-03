from django.db import models
from django.shortcuts import render
from typing import Any, Dict
from django.db.models.query import QuerySet
from .models import Entry, PassDown
from UserBase.models import WorkCenter
from .forms import PassDownForm, EntryForm
from django.urls import reverse
from django.views.generic import (
    CreateView, ListView, DetailView, TemplateView, UpdateView,
    DeleteView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .mixins import AdministratorAndLoginRequiredMixin


class EntryCreateView(LoginRequiredMixin, CreateView):
    template_name = "passdown/entry_create.html"
    form_class = EntryForm
    context_object_name = 'passdown'

    def get_queryset(self):
        queryset = PassDown.objects.last()
        return queryset

    def get_success_url(self):
        return reverse("passdown:entry-create")


class PassDownCreateView(LoginRequiredMixin, CreateView):
    template_name = "passdown/passdown_create.html"
    form_class = PassDownForm

    def form_valid(self, form):
        entered = form.save(commit=False)
        entered.entered_by = self.request.user
        entered.work_center = self.request.user.work_center
        entered.save()
        return super(PassDownCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse("passdown:entry-create")
    
    
    
class MasterListView2(LoginRequiredMixin, ListView):
    template_name = 'passdown/master_list2.html'
    model = PassDown
    paginate_by = 5
    context_object_name = 'entries'


    def get_queryset(self):
        user = self.request.user

        queryset = PassDown.objects.filter(work_center = user.work_center).order_by("-date_time")
        return queryset
    

# This search view returns the entire passdown that contains the queried entry
class SearchResultsView(LoginRequiredMixin, ListView):
    template_name = 'passdown/search_results.html'
    model = PassDown
    paginate_by = 5
    context_object_name = 'entries'
    form_class = EntryForm

    def get_queryset(self):
        modex = self.request.GET.get('modex')
        shift = self.request.GET.get('shift')
        keyword = self.request.GET.get('keyword')
        job_status = self.request.GET.get('jobstatus')
        #cdi = self.request.GET.get('cdi')
        discrepancy = self.request.GET.get('discrepancy')
        queryset = PassDown.objects.filter(
            Q(entry__modex__icontains=modex),
            Q(shift__icontains=shift),
            Q(entry__text_body__icontains=keyword),
            #Q(entry__job_status__icontains=job_status),
            #Q(entry__cdi__icontains=cdi),
            Q(entry__discrepancy__icontains=discrepancy)
            )
        return queryset

# This search view returns only the queried entries.    
class SearchResultsEntryView(LoginRequiredMixin, ListView):
    template_name = 'passdown/search_results_by_entry.html'
    model = Entry
    paginate_by = 10
    context_object_name = 'entries'

    def get_queryset(self):
        user = self.request.user

        modex = self.request.GET.get('modex')
        shift = self.request.GET.get('shift')
        keyword = self.request.GET.get('keyword')
        job_status = self.request.GET.get('jobstatus')
        cdi = self.request.GET.get('cdi')
        discrepancy = self.request.GET.get('discrepancy')
        queryset = Entry.objects.filter(
            Q(passdown__work_center = user.work_center),
            Q(modex__icontains=modex),
            Q(passdown__shift__icontains=shift),
            Q(text_body__icontains=keyword),
            Q(job_status__icontains=job_status),
            Q(cdi__icontains=cdi),
            Q(discrepancy__icontains=discrepancy)
            )
        return queryset


class SearchView(LoginRequiredMixin, TemplateView):
    template_name = 'passdown/search.html'

class AdminDashboardView(AdministratorAndLoginRequiredMixin, ListView):
     template_name = 'passdown/admin_dashboard.html'
     model = WorkCenter
     context_object_name = 'workcenter'

class NoPermissionView(TemplateView):
    template_name = 'passdown/no_permission.html'

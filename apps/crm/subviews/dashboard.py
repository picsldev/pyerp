from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .lead import PyLead

def DashboardCrmView(request):
    leads = PyLead.objects.all()
    return render(request, 'crm/dashboard-crm.html', {
        'leads': leads,
        'total_leads': leads,
        'new_leads': leads.filter(stage_id__name__iexact='nuevo'),
        'gained_leads': leads.filter(stage_id__name__iexact='ganado'),
        'lost_leads': leads.filter(stage_id__name__iexact='perdidos')
    })
from django.shortcuts import render
from django.views import generic
from .models import Lead


class LeadList(generic.ListView):
    template_name = 'leads/lead-list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetails(generic.DetailView):
    template_name = 'leads/lead-details.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'
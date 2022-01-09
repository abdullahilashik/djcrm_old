from django.shortcuts import render, reverse
from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm
from django.contrib import messages


class LeadList(generic.ListView):
    template_name = 'leads/lead-list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'
    paginate_by = 10


class LeadDetails(generic.DetailView):
    template_name = 'leads/lead-details.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreate(generic.CreateView):
    template_name = 'leads/lead-create.html'
    form_class = LeadForm

    # queryset = Lead.objects.all()
    # context_object_name = 'lead'

    def get_success_url(self):
        messages.success(self.request, 'New lead created successfully!')
        return reverse('leads:lead-list')


class LeadUpdate(generic.UpdateView):
    template_name = 'leads/lead-update.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'
    form_class = LeadForm

    def get_success_url(self):
        messages.info(self.request, 'Lead successfully updated!')
        return reverse('leads:lead-list')


class LeadDelete(generic.DeleteView):
    template_name = 'leads/lead-delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        messages.error(self.request, 'Lead has been removed!')
        return reverse('leads:lead-list')

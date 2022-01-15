from django.shortcuts import render, reverse
from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm
from django.contrib import messages
from .mixins import OrganizationLoginRequiredMixin


class LeadList(OrganizationLoginRequiredMixin, generic.ListView):
    template_name = 'leads/lead-list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'
    paginate_by = 10


class LeadDetails(OrganizationLoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead-details.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreate(OrganizationLoginRequiredMixin, generic.CreateView):
    template_name = 'leads/lead-create.html'
    form_class = LeadForm

    # queryset = Lead.objects.all()
    # context_object_name = 'lead'

    def get_success_url(self):
        messages.success(self.request, 'New lead created successfully!')
        return reverse('leads:lead-list')


class LeadUpdate(OrganizationLoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead-update.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'
    form_class = LeadForm

    def get_success_url(self):
        messages.info(self.request, 'Lead successfully updated!')
        return reverse('leads:lead-list')


class LeadDelete(OrganizationLoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead-delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        messages.error(self.request, 'Lead has been removed!')
        return reverse('leads:lead-list')

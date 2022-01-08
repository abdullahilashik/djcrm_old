from django.shortcuts import render, reverse
from django.views import generic
from .models import Lead
from .forms import LeadForm


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
        return reverse('leads:lead-list')


class LeadUpdate(generic.UpdateView):
    template_name = 'leads/lead-update.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDelete(generic.DeleteView):
    template_name = 'leads/lead-delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return redirect('leads:lead-list')

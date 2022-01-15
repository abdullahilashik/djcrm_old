from django.shortcuts import render, reverse
from django.views import generic
from leads.models import Agent
from .forms import AgentForm
from django.contrib import messages

class AgentListView(generic.ListView):
    template_name = 'agents/agent-list.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'


class AgentDetailsView(generic.DetailView):
    template_name = 'agents/agent-details.html'
    queryset = Agent.objects.all()


class AgentDeleteView(generic.DeleteView):
    template_name = 'agents/agent-delete.html'
    queryset = Agent.objects.all()

    def get_success_url(self):
        messages.error(self.request, 'Agent has been removed along with created leads!')
        return reverse('agents:agent-list')


class AgentCreateView(generic.CreateView):
    template_name = 'agents/agent-create.html'
    queryset = Agent.objects.all()
    form_class = AgentForm

    # context_object_name = ''

    def get_success_url(self):
        messages.success(self.request, 'New agent has been created!')
        return reverse('agents:agent-list')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        # messages.success(self.request, 'New agent has been created!')
        return super(AgentCreateView, self).form_valid(form)


class AgentUpdateView(generic.UpdateView):
    template_name = 'agents/agent-update.html'
    queryset = Agent.objects.all()
    form_class = AgentForm

    # context_object_name = ''

    def get_success_url(self):
        messages.success(self.request, 'Agent information has been updated!')
        return reverse('agents:agent-list')

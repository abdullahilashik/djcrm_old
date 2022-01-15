from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailsView, AgentDeleteView, AgentUpdateView

app_name = 'agents'

urlpatterns = [
    path('agent-list/', AgentListView.as_view(), name='agent-list'),
    path('agent-create/', AgentCreateView.as_view(), name='agent-create'),
    path('agent-create/details/<int:pk>', AgentDetailsView.as_view(), name='agent-details'),
    path('agent-create/delete/<int:pk>', AgentDeleteView.as_view(), name='agent-delete'),
    path('agent-create/update/<int:pk>', AgentUpdateView.as_view(), name='agent-update'),
]

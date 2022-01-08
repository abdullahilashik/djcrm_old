from django.urls import path
from .views import (
    LeadList, LeadDetails, LeadUpdate, LeadCreate, LeadDelete
)

app_name = 'leads'
urlpatterns = [
    path('lead-list/', LeadList.as_view(), name='lead-list'),
    path('lead-details/<int:pk>/', LeadDetails.as_view(), name='lead-details'),
    path('lead-update/<int:pk>/', LeadUpdate.as_view(), name='lead-update'),
    path('lead-delete/<int:pk>/', LeadDelete.as_view(), name='lead-delete'),
    path('lead-create/', LeadCreate.as_view(), name='lead-create'),
]

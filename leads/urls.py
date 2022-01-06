from django.urls import path
from .views import (
    LeadList, LeadDetails
)

app_name = 'leads'
urlpatterns = [
    path('lead-list/', LeadList.as_view(), name='lead-list'),
    path('lead-details/<int:pk>/', LeadDetails.as_view(), name='lead-details'),
]

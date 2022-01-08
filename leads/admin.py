from django.contrib import admin
from .models import Lead, Agent


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    pass


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    pass

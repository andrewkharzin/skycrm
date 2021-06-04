from django.contrib import admin
from .models import Agent


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'agent_type',
        'company',
        'department'
    ]

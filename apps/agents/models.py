from django.db import models
from apps.users.models import User
from apps.profiles.models import Profile
from apps.companies.models import Company, Department


class Agent(models.Model):
    AGENT_TYPE = (
        ('AirlineAgent', 'AirlineAgent'),
        ('WRHAgent', 'WRHAgent'),
        ('AirportAgent', 'AirportAgent')
    )
    agent_type = models.CharField(
        max_length=100, blank=True, null=True, choices=AGENT_TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.email

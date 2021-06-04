from django.contrib import admin
from apps.users.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'first_name',
        'last_name',
        'position',
        'email',
        'phone_number',
        'birth_date',
        'location',
        'avatar_tag',
        'date_join'
    ]
    readonly_fields = ('avatar_tag',)

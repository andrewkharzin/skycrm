from django.contrib import admin
from apps.users.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'full_name',
        'position',
        'email',
        'phone_number',
        'birth_date',
        'location',
        'date_join',
        'avatar_tag',
    ]
    readonly_fields = ('avatar_tag',)

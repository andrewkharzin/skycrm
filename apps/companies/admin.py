from django.contrib import admin
from .models import Company, Department


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        'company_name',
        'location',
        'contact_phone',
        'cmp_logo_tag',


    ]


@admin.register(Department)
class DevAdmin(admin.ModelAdmin):
    list_display = [
        'dep_name',

    ]

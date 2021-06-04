from django.db import models
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from thumbnails.fields import ImageField
from django.utils.html import escape
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


def upload_to(instance, filename):
    return 'companylogo/%s' % filename


class Company(models.Model):
    company_name = models.CharField(max_length=100,)
    alias = models.SlugField()

    location = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = PhoneNumberField()
    company_logo = models.ImageField(
        verbose_name=_('Logo'), upload_to='company_logo', null=True, blank=True
    )

    def __str__(self):
        return self.alias

    def get_company_logo(self):
        if not self.company_logo:
            return '/static/images/default_user.png'
        return self.company_logo.url

    # method to create a fake table field in read only mode
    def cmp_logo_tag(self):
        return mark_safe('<img src="%s" width="80" height="80" />' % self.get_company_logo())

    cmp_logo_tag.short_description = 'Company Logo'


class Department(models.Model):
    dep_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Department')
    # alias = models.SlugField()
    parent_org = models.ForeignKey(Company, on_delete=models.CASCADE)

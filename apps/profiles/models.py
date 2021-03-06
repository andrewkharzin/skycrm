from django.db import models
from django.db.models.expressions import F
from apps.users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from thumbnails.fields import ImageField
from django.utils.html import escape
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


def upload_to(instance, filename):
    return 'avatars/%s' % filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55, null=True, blank=True)
    last_name = models.CharField(max_length=55, null=True, blank=True)
    # company =
    position = models.CharField(max_length=75, blank=True, null=True)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=55, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(
        verbose_name=_('Avatar'), upload_to='user_profilesphotos', null=True, blank=True
    )
    date_join = models.DateField(auto_now_add=True)

    def _get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)

    def __str__(self):
        return self.full_name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    # Here I return the avatar or picture with an owl, if the avatar is not selected

    def get_avatar(self):
        if not self.avatar:
            return '/static/images/default_user.png'
        return self.avatar.url

    # method to create a fake table field in read only mode
    def avatar_tag(self):
        return mark_safe('<img src="%s" width="80" height="80" />' % self.get_avatar())

    avatar_tag.short_description = 'Avatar'

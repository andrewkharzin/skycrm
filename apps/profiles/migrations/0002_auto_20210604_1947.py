# Generated by Django 3.2.3 on 2021-06-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_profilesphotos', verbose_name='Avatar'),
        ),
    ]
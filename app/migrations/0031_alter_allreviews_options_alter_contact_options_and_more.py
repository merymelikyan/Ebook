# Generated by Django 5.1 on 2024-10-01 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_reviewsmembers_delete_reviewsmambers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allreviews',
            options={'verbose_name': 'All Reviews', 'verbose_name_plural': 'All Reviews'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='meetauther',
            options={'verbose_name': 'Meet Auther', 'verbose_name_plural': 'Meet Auther'},
        ),
        migrations.AlterModelOptions(
            name='socialsname',
            options={'verbose_name': 'Socials Name', 'verbose_name_plural': 'Socials Name'},
        ),
    ]

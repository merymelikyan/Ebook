# Generated by Django 5.1 on 2024-10-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_alter_allreviews_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='stars',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]

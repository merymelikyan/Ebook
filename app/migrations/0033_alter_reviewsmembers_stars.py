# Generated by Django 5.1 on 2024-10-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_reviews_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewsmembers',
            name='stars',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]

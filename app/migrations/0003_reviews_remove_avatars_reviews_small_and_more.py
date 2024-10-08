# Generated by Django 5.1.1 on 2024-09-06 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_avatars_booksection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews_stars', models.FloatField()),
                ('reviews_smoll', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'reviews',
                'verbose_name_plural': 'reviews',
            },
        ),
        migrations.RemoveField(
            model_name='avatars',
            name='reviews_small',
        ),
        migrations.RemoveField(
            model_name='avatars',
            name='reviews_stars',
        ),
    ]

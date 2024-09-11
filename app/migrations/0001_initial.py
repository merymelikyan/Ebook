# Generated by Django 5.1.1 on 2024-09-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Footer Text',
                'verbose_name_plural': 'Footer Text',
            },
        ),
        migrations.CreateModel(
            name='HeaderText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='header_text')),
            ],
            options={
                'verbose_name': 'Header Text',
                'verbose_name_plural': 'Header Texts',
            },
        ),
    ]

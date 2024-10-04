# Generated by Django 5.1 on 2024-10-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_delete_contentblock_remove_reviews_stars_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewsMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('position', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='reviews_members')),
                ('stars', models.FloatField()),
                ('reviews_class1', models.CharField(blank=True, max_length=40, null=True)),
                ('reviews_class2', models.CharField(blank=True, max_length=40, null=True)),
                ('reviews_class3', models.CharField(blank=True, max_length=40, null=True)),
                ('reviews_class4', models.CharField(blank=True, max_length=40, null=True)),
                ('reviews_class5', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Reviews Members',
                'verbose_name_plural': 'Reviews Members',
            },
        ),
        migrations.DeleteModel(
            name='ReviewsMambers',
        ),
        migrations.AlterModelOptions(
            name='contactsname',
            options={'verbose_name': 'Contacts Name', 'verbose_name_plural': 'Contacts Name'},
        ),
    ]

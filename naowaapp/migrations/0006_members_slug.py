# Generated by Django 3.1.1 on 2021-03-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naowaapp', '0005_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='slug',
            field=models.SlugField(default=0, unique=True),
        ),
    ]

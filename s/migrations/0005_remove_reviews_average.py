# Generated by Django 2.2.8 on 2020-01-12 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s', '0004_reviews_average'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='average',
        ),
    ]

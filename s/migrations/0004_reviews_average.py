# Generated by Django 2.2.8 on 2020-01-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s', '0003_auto_20200112_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='average',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

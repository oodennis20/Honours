# Generated by Django 2.2.8 on 2020-01-12 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s', '0002_auto_20200112_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='s.Project'),
        ),
    ]

# Generated by Django 4.2 on 2023-04-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationmodule',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

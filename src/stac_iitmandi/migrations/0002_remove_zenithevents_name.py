# Generated by Django 3.1.2 on 2020-12-29 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stac_iitmandi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zenithevents',
            name='name',
        ),
    ]

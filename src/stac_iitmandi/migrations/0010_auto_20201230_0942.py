# Generated by Django 3.1.2 on 2020-12-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stac_iitmandi', '0009_utkarshevents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zenithevents',
            name='problem_statement',
            field=models.URLField(blank=True, default='about:blank', null=True),
        ),
    ]

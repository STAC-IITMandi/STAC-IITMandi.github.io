# Generated by Django 3.1.2 on 2020-12-31 20:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stac_iitmandi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=50, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='Astrax')),
            ],
        ),
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fb', models.URLField(blank=True, default='#/')),
                ('insta', models.URLField(blank=True, default='#/')),
                ('git', models.URLField(blank=True, default='#/')),
                ('linkedin', models.URLField(blank=True, default='#/')),
                ('image', models.ImageField(default='default.jpg', upload_to='Alumni')),
            ],
        ),
        migrations.CreateModel(
            name='Astrax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, unique=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='Astrax')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='photogallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, unique=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='Gallery/Photogallery')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pleiades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, unique=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='Pleiades')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('problem_statement', models.URLField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='videogallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, unique=True)),
                ('link', models.URLField(blank=True, default='#/')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='Gallery/Videogallery')),
            ],
        ),
        migrations.AlterField(
            model_name='coordinators',
            name='fb',
            field=models.URLField(blank=True, default='#/'),
        ),
        migrations.AlterField(
            model_name='coordinators',
            name='git',
            field=models.URLField(blank=True, default='#/'),
        ),
        migrations.AlterField(
            model_name='coordinators',
            name='insta',
            field=models.URLField(blank=True, default='#/'),
        ),
        migrations.AlterField(
            model_name='coordinators',
            name='linkedin',
            field=models.URLField(blank=True, default='#/'),
        ),
        migrations.AlterField(
            model_name='core_team',
            name='fb',
            field=models.URLField(blank=True, default='#/'),
        ),
        migrations.AlterField(
            model_name='core_team',
            name='git',
            field=models.URLField(blank=True, default='#/'),
        ),
        migrations.AlterField(
            model_name='core_team',
            name='insta',
            field=models.URLField(blank=True, default='#/'),
        ),
        migrations.AlterField(
            model_name='core_team',
            name='linkedin',
            field=models.URLField(blank=True, default='#/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genealogy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='handle',
            field=models.CharField(blank=True, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(help_text=b'Uniq key for Django app', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='family',
            name='handle',
            field=models.CharField(blank=True, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='id',
            field=models.AutoField(help_text=b'Uniq key for Django app', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='media',
            name='handle',
            field=models.CharField(blank=True, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='id',
            field=models.AutoField(help_text=b'Uniq key for Django app', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='handle',
            field=models.CharField(blank=True, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(help_text=b'Uniq key for Django app', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='handle',
            field=models.CharField(blank=True, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(help_text=b'Uniq key for Django app', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='place',
            name='handle',
            field=models.CharField(blank=True, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.AutoField(help_text=b'Uniq key for Django app', primary_key=True, serialize=False),
        ),
    ]
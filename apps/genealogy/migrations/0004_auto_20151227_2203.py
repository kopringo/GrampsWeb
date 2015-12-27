# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genealogy', '0003_auto_20151227_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='long',
            new_name='lng',
        ),
        migrations.AlterField(
            model_name='event',
            name='handle',
            field=models.CharField(blank=True, default=None, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='handle',
            field=models.CharField(blank=True, default=None, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='handle',
            field=models.CharField(blank=True, default=None, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='handle',
            field=models.CharField(blank=True, default=None, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='handle',
            field=models.CharField(blank=True, default=None, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='handle',
            field=models.CharField(blank=True, default=None, help_text=b'Uniq handler for remote databases', max_length=32, unique=True),
        ),
    ]

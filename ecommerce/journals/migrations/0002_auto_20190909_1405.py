# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-09 14:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    def remove_journals(apps, schema_editor):
        """Delete any existing offer conditions that have journals"""
        Condition = apps.get_model('offer', 'Condition')
        Condition.objects.filter(journal_bundle_uuid__isnull=False).delete()

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(remove_journals, migrations.RunPython.noop),
    ]
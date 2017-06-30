# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-29 20:09
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judgment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='judgement',
            name='timeActive',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[], null=True),
        ),
        migrations.AddField(
            model_name='judgement',
            name='timeAway',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[], null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-04 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CAL', '0006_auto_20170504_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judgement',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='judgement',
            name='user',
        ),
        migrations.DeleteModel(
            name='Judgement',
        ),
    ]

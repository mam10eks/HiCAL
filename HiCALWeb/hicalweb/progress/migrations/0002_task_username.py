# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-07-27 00:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('progress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

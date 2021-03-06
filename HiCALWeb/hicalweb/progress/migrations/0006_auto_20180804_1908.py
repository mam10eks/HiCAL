# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-08-04 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0005_task_strategy'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='show_full_document_content',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='strategy',
            field=models.CharField(choices=[('doc', 'Full document (CAL)'), ('para', 'Paragraph (CAL)'), ('para_scal', 'Paragraph (S-CAL)')], max_length=64),
        ),
    ]

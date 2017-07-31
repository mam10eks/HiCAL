# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-02 16:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('', ''), ('MALE', 'Male'), ('FEMALE', 'Female')], max_length=56)),
                ('student_degree', models.CharField(choices=[('', ''), ('UNDERGRAD', 'An undergraduate student'), ('GRAD', 'A graduate student'), ('OTHER', 'Other. Please specify')], max_length=56)),
                ('student_degree_other', models.CharField(blank=True, max_length=128, null=True)),
                ('student_major', models.CharField(choices=[('', ''), ('ART', 'An art student'), ('STEM', 'A science, technology, engineering, or math student.'), ('OTHER', 'Other. Please specify')], max_length=56)),
                ('student_major_other', models.CharField(blank=True, max_length=128, null=True)),
                ('language', models.CharField(choices=[('', ''), ('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCE', 'Advance'), ('FLUENT', 'Fluent'), ('PROFICIENT', 'Proficient'), ('NATIVE', 'Native')], max_length=56)),
                ('search_engine_usage', models.CharField(choices=[('', ''), ('SEVERAL', 'Several times a day'), ('ONCE', 'At least once a day'), ('WEEK', 'At least once a week'), ('MONTH', 'At least once a month'), ('RARELY', 'Rarely (Less than one search a month on average)')], max_length=56)),
                ('expertise', models.CharField(choices=[('', ''), ('STRONG_DISAGREE', 'Strongly Disagree'), ('DISAGREE', 'Disagree'), ('NEUTRAL', 'Neutral'), ('AGREE', 'Agree'), ('STRONGLY_AGREE', 'Strongly Agree')], max_length=56)),
                ('trouble', models.CharField(choices=[('', ''), ('STRONG_DISAGREE', 'Strongly Disagree'), ('DISAGREE', 'Disagree'), ('NEUTRAL', 'Neutral'), ('AGREE', 'Agree'), ('STRONGLY_AGREE', 'Strongly Agree')], max_length=56)),
                ('help', models.CharField(choices=[('', ''), ('STRONG_DISAGREE', 'Strongly Disagree'), ('DISAGREE', 'Disagree'), ('NEUTRAL', 'Neutral'), ('AGREE', 'Agree'), ('STRONGLY_AGREE', 'Strongly Agree')], max_length=56)),
                ('enjoyment', models.CharField(choices=[('', ''), ('STRONG_DISAGREE', 'Strongly Disagree'), ('DISAGREE', 'Disagree'), ('NEUTRAL', 'Neutral'), ('AGREE', 'Agree'), ('STRONGLY_AGREE', 'Strongly Agree')], max_length=56)),
                ('training', models.CharField(choices=[('', ''), ('YES', 'Yes'), ('NO', 'No')], max_length=56)),
                ('training_feedback', models.TextField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(choices=[('---', '---'), ('NOT AT ALL', 'Not at all'), ('SLIGHTLY', 'Slightly'), ('SOMEWHAT', 'Somewhat'), ('MODERATELY', 'Moderately'), ('EXTREMELY', 'Extremely')], default='---', max_length=35)),
                ('confidence', models.CharField(choices=[('---', '---'), ('NOT AT ALL', 'Not at all'), ('SLIGHTLY', 'Slightly'), ('SOMEWHAT', 'Somewhat'), ('MODERATELY', 'Moderately'), ('EXTREMELY', 'Extremely')], default='---', max_length=35)),
                ('mood', models.CharField(choices=[('---', '---'), ('NOT AT ALL', 'Not at all'), ('SLIGHTLY', 'Slightly'), ('SOMEWHAT', 'Somewhat'), ('MODERATELY', 'Moderately'), ('EXTREMELY', 'Extremely')], default='---', max_length=35)),
                ('experience', models.CharField(choices=[('---', '---'), ('NOT AT ALL', 'Not at all'), ('SLIGHTLY', 'Slightly'), ('SOMEWHAT', 'Somewhat'), ('MODERATELY', 'Moderately'), ('EXTREMELY', 'Extremely')], default='---', max_length=35)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familiarity', models.CharField(choices=[('---', '---'), ('NOT AT ALL', 'Not at all'), ('SLIGHTLY', 'Slightly'), ('SOMEWHAT', 'Somewhat'), ('MODERATELY', 'Moderately'), ('EXTREMELY', 'Extremely')], default='---', max_length=35)),
                ('difficulty', models.CharField(choices=[('---', '---'), ('NOT AT ALL', 'Not at all'), ('SLIGHTLY', 'Slightly'), ('SOMEWHAT', 'Somewhat'), ('MODERATELY', 'Moderately'), ('EXTREMELY', 'Extremely')], default='---', max_length=35)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('timespent', models.DurationField(default=datetime.timedelta)),
                ('posttask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_posttask', to='progress.PostTask')),
                ('pretask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_pretask', to='progress.PreTask')),
            ],
        ),
        migrations.CreateModel(
            name='TaskSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_search', models.BooleanField()),
                ('show_CAL', models.BooleanField()),
                ('toggle_doc', models.BooleanField()),
                ('only_show_doc', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='setting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='progress.TaskSetting'),
        ),
        migrations.AddField(
            model_name='task',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic'),
        ),
    ]
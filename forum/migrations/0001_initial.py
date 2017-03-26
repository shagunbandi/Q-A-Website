# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(max_length=10000)),
                ('ans_author', models.CharField(max_length=30)),
                ('ans_date', models.DateTimeField(default=datetime.datetime(2017, 3, 26, 14, 25, 18, 316240), blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=10000)),
                ('ques_author', models.CharField(max_length=30)),
                ('ques_date', models.DateTimeField(default=datetime.datetime(2017, 3, 26, 14, 25, 18, 315788), blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='forum.Question'),
        ),
    ]

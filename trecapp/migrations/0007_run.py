# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0006_researcher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('result_file', models.FileField(upload_to=b'/media/results')),
                ('run_type', models.IntegerField(default=0, choices=[(0, b'Automatic'), (1, b'Manual')])),
                ('query_type', models.IntegerField(default=4, choices=[(0, b'Title'), (1, b'Title + Description'), (2, b'Description'), (3, b'All'), (4, b'Other')])),
                ('feedback_type', models.IntegerField(default=0, choices=[(0, b'None'), (1, b'Pseudo'), (2, b'Relevance'), (3, b'Other')])),
                ('map', models.FloatField()),
                ('p10', models.FloatField()),
                ('p20', models.FloatField()),
                ('researcher', models.ForeignKey(to='trecapp.Researcher')),
                ('task', models.ForeignKey(to='trecapp.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

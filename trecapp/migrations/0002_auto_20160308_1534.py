# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='track_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]

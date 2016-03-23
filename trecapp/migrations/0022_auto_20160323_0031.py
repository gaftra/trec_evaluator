# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0021_auto_20160320_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='run',
        ),
        migrations.DeleteModel(
            name='Leaderboard',
        ),
    ]

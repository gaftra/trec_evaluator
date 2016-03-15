# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0010_auto_20160315_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='map',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='p10',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='p20',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]

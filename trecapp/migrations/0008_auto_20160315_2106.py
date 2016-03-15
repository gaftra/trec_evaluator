# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0007_run'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='description',
            field=models.CharField(default=b'', max_length=512),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='name',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]

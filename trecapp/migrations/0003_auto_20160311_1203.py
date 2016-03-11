# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0002_auto_20160308_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='judgementFile',
            field=models.FileField(upload_to=b'/media/data'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]

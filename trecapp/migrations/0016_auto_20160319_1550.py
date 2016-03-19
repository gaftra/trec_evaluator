# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0015_auto_20160316_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='profile_picture',
            field=models.ImageField(default='', upload_to=b'/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researcher',
            name='website',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='researcher',
            name='display_name',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
    ]

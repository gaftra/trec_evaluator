# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0003_auto_20160311_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]

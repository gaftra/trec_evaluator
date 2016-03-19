# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import trecapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0019_auto_20160319_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher',
            name='profile_picture',
            field=models.ImageField(default=b'profile_pic.png', upload_to=trecapp.models.upload_dir),
            preserve_default=True,
        ),
    ]

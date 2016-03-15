# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0012_auto_20160315_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='result_file',
            field=models.FileField(upload_to=b'media/results'),
            preserve_default=True,
        ),
    ]

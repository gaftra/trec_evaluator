# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0008_auto_20160315_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='description',
            field=models.CharField(default=b'', max_length=512, null=True),
            preserve_default=True,
        ),
    ]

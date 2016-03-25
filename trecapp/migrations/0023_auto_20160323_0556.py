# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0022_auto_20160323_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='judgementFile',
            field=models.FileField(upload_to=b'media/data'),
            preserve_default=True,
        ),
    ]

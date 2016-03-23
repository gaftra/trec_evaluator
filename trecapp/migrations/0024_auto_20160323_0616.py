# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0023_auto_20160323_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='judgementFile',
            field=models.FileField(upload_to=b'data'),
            preserve_default=True,
        ),
    ]

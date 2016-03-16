# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trecapp', '0014_auto_20160315_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researcher',
            name='password',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='username',
        ),
        migrations.AddField(
            model_name='researcher',
            name='display_name',
            field=models.CharField(default='', unique=True, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researcher',
            name='organization',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='researcher',
            name='user',
            field=models.OneToOneField(default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='run',
            name='result_file',
            field=models.FileField(upload_to=b'results/'),
            preserve_default=True,
        ),
    ]

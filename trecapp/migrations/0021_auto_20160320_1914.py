# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import trecapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('trecapp', '0020_auto_20160319_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('researcher_name', models.CharField(max_length=64, null=True)),
                ('map', models.FloatField(default=0.0, null=True)),
                ('p10', models.FloatField(default=0.0, null=True)),
                ('p20', models.FloatField(default=0.0, null=True)),
                ('run', models.ForeignKey(to='trecapp.Run')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='display_name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='researcher',
            name='organization',
            field=models.CharField(max_length=512),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='researcher',
            name='profile_picture',
            field=models.ImageField(default=b'profile_pic.png', upload_to=trecapp.models.upload_dir, blank=True),
            preserve_default=True,
        ),
    ]

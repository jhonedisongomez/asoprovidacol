# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-03 20:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_auto_20160502_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 5, 3, 15, 54, 10, 117791)),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-31 23:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0011_auto_20160531_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupschedule',
            name='count',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
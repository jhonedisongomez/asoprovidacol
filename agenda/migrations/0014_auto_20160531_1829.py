# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-31 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0013_auto_20160531_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupschedule',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

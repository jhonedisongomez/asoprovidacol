# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-01 15:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0014_auto_20160531_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupschedule',
            old_name='active',
            new_name='action',
        ),
        migrations.RemoveField(
            model_name='signupschedule',
            name='fk_user_modified',
        ),
        migrations.RemoveField(
            model_name='signupschedule',
            name='modified_at',
        ),
        migrations.AlterField(
            model_name='signupschedule',
            name='count',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
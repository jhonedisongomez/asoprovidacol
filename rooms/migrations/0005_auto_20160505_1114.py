# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-05 16:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_remove_room_fk_congress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityroom',
            name='fk_user_created',
        ),
        migrations.RemoveField(
            model_name='activityroom',
            name='fk_user_modified',
        ),
        migrations.DeleteModel(
            name='ActivityRoom',
        ),
    ]

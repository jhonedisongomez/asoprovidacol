# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-05 15:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_auto_20160502_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomtopic',
            name='fk_user_created',
        ),
        migrations.RemoveField(
            model_name='roomtopic',
            name='fk_user_modified',
        ),
        migrations.DeleteModel(
            name='RoomTopic',
        ),
    ]

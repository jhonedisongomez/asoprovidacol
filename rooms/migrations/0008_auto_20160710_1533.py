# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-10 20:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_auto_20160626_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='fk_section_type_code',
            new_name='fk_section_code',
        ),
    ]

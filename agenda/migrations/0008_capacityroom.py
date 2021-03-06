# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-31 22:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0007_auto_20160526_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='capacityRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity_room_code', models.CharField(default=uuid.uuid4, max_length=64)),
                ('list_place', models.CharField(max_length=700)),
                ('action', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('fk_sign_up_schedule_code', models.CharField(max_length=64)),
                ('fk_user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capacity_room_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

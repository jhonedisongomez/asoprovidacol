# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-02 19:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0002_auto_20160501_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_agenda_code', models.CharField(default=uuid.uuid4, max_length=64)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('fk_agenda_code', models.CharField(max_length=64)),
                ('fk_topic_code', models.CharField(max_length=64)),
                ('fk_user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_agenda_creator', to=settings.AUTH_USER_MODEL)),
                ('fk_user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_agenda_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='signupschedule',
            old_name='fk_agenda',
            new_name='fk_topic_agenda',
        ),
        migrations.RemoveField(
            model_name='signupschedule',
            name='fk_professor_activity',
        ),
    ]

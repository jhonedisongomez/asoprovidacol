# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-30 23:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_code', models.CharField(default=uuid.uuid4, max_length=64)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('fk_user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_creator', to=settings.AUTH_USER_MODEL)),
                ('fk_user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('fk_project_code', models.CharField(max_length=64)),
                ('fk_user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_user_creator', to=settings.AUTH_USER_MODEL)),
                ('fk_user_exponent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_user_exponent', to=settings.AUTH_USER_MODEL)),
                ('fk_user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_user_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

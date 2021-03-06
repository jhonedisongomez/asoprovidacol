# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-10 20:33
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
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(blank=True, default=uuid.uuid4, max_length=64)),
                ('country_name', models.CharField(max_length=64)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('fk_user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_creator', to=settings.AUTH_USER_MODEL)),
                ('fk_user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_code', models.CharField(default=uuid.uuid4, max_length=64, null=True)),
                ('section_name', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('fk_country_code', models.CharField(max_length=64, null=True)),
                ('fk_section_code', models.CharField(blank=True, max_length=64, null=True)),
                ('fk_section_type_code', models.CharField(max_length=64, null=True)),
                ('fk_user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_creator', to=settings.AUTH_USER_MODEL)),
                ('fk_user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='sectionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_type_code', models.CharField(default=uuid.uuid4, max_length=64, null=True)),
                ('section_type_name', models.CharField(max_length=40, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('fk_user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_type_creator', to=settings.AUTH_USER_MODEL)),
                ('fk_user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_type_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

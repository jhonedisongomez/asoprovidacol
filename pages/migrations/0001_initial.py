# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-14 17:10
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
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_code', models.CharField(default=uuid.uuid4, max_length=64)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('fk_user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_creator', to=settings.AUTH_USER_MODEL)),
                ('fk_user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_image_code', models.CharField(default=uuid.uuid4, max_length=64)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('fk_page_code', models.CharField(max_length=64)),
                ('fk_user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_image_creator', to=settings.AUTH_USER_MODEL)),
                ('fk_user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_image_updater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

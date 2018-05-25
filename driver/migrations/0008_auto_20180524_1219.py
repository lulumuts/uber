# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 09:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0007_auto_20180524_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='driver_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 12:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0019_auto_20180527_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='driver_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

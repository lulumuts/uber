# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 04:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('driver', '0011_auto_20180524_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0002_auto_20180519_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='driver_image',
            field=models.ImageField(blank=True, upload_to='rider/'),
        ),
    ]

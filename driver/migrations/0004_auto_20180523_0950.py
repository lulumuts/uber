# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 06:50
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_delete_worldborder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickup_location',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]

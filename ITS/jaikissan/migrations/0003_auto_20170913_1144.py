# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaikissan', '0002_kissan_k_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='Lat_5',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farm',
            name='Lat_6',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farm',
            name='Lat_7',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farm',
            name='Lat_8',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farm',
            name='Long_5',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farm',
            name='Long_6',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farm',
            name='Long_7',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farm',
            name='Long_8',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]

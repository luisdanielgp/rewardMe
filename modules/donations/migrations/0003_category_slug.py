# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-21 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_auto_20171119_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('love', '0002_auto_20160120_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=2, unique=True),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-15 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170315_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='title',
            field=models.CharField(blank=True, default='', max_length=512, null=True),
        ),
    ]
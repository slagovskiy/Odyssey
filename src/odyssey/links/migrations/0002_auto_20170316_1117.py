# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-16 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylink',
            name='link',
            field=models.CharField(default='', max_length=255),
        ),
    ]

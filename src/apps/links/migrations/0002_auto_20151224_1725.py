# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylinks',
            name='link',
            field=models.URLField(default=''),
        ),
    ]
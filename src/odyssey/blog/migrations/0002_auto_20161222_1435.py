# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 07:35
from __future__ import unicode_literals

from django.db import migrations, models
import odyssey.blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='social_image',
            field=models.ImageField(blank=True, null=True, upload_to=odyssey.blog.models.Post.images_path, verbose_name='Social image'),
        ),
        migrations.AddField(
            model_name='post',
            name='uid',
            field=models.TextField(blank=True, max_length=40, null=True),
        ),
    ]
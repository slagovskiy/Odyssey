# Generated by Django 2.2.2 on 2019-07-02 09:05

from django.db import migrations, models
import django.db.models.deletion
import odyssey.media.models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, null=True, upload_to=odyssey.media.models.MediaFile.mediafile_path, verbose_name='File')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='media.MediaFolder')),
            ],
            options={
                'verbose_name': 'Media File',
                'verbose_name_plural': 'Media Files',
                'ordering': ['created'],
            },
        ),
    ]

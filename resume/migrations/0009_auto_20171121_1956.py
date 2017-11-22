# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20171117_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.IntegerField(default=0, help_text='0 - 100'),
        ),
    ]

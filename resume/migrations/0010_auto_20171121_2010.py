# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_auto_20171121_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='resume_profile/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-14 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20180104_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posted_on',
        ),
    ]

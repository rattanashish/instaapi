# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-21 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_followfollowing_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='followfollowing',
            name='user_name_follow',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

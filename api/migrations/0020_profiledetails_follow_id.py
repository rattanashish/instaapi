# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-27 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20171224_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetails',
            name='follow_id',
            field=models.IntegerField(null=True),
        ),
    ]
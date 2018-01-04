# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-04 12:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20171227_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]

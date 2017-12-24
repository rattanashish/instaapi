# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-21 11:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20171221_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_follow', to=settings.AUTH_USER_MODEL),
        ),
    ]

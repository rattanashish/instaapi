# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-21 12:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20171221_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followfollowing',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

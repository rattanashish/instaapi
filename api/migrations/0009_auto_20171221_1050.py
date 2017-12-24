# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-21 10:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_profiledetails_post_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow', models.ManyToManyField(related_name='followed_by', to='api.followers')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_follow', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='profie_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profilefield', to='api.profiledetails'),
            preserve_default=False,
        ),
    ]

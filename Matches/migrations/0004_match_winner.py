# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-21 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20180820_1310'),
        ('Matches', '0003_match_tournament_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='Home.Team'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ping',
            name='local_ip',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ping',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pings', to='api.Server'),
        ),
    ]
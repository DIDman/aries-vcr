# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-07 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0008_auto_20180829_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='credential_def_id',
            field=models.TextField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='credentialtype',
            name='credential_def_id',
            field=models.TextField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='credential',
            name='revoked',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='credential',
            name='wallet_id',
            field=models.TextField(db_index=True),
        ),
    ]
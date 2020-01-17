# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-07 19:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("api_v2", "0019_credentialtype_url")]

    operations = [
        migrations.AlterModelOptions(name="address", options={"ordering": ("id",)}),
        migrations.AlterModelOptions(name="attribute", options={"ordering": ("id",)}),
        migrations.AlterModelOptions(name="claim", options={"ordering": ("id",)}),
        migrations.AlterModelOptions(name="credential", options={"ordering": ("id",)}),
        migrations.AlterModelOptions(
            name="credentialset", options={"ordering": ("id",)}
        ),
        migrations.AlterModelOptions(
            name="credentialtype", options={"ordering": ("id",)}
        ),
        migrations.AlterModelOptions(name="issuer", options={"ordering": ("id",)}),
        migrations.AlterModelOptions(name="name", options={"ordering": ("id",)}),
        migrations.AlterModelOptions(name="schema", options={"ordering": ("id",)}),
        migrations.AlterModelOptions(name="topic", options={"ordering": ("id",)}),
        migrations.AlterModelOptions(
            name="topicrelationship", options={"ordering": ("id",)}
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-17 02:24
from __future__ import unicode_literals

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20170316_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_text',
            name='text',
            field=froala_editor.fields.FroalaField(blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='text',
            field=froala_editor.fields.FroalaField(blank=True),
        ),
        migrations.AlterField(
            model_name='submission_guidelines',
            name='text',
            field=froala_editor.fields.FroalaField(blank=True),
        ),
    ]

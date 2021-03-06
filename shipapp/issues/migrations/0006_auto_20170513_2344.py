# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_auto_20170505_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='parent_issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='issues.Issue'),
        ),
        migrations.AlterField(
            model_name='image',
            name='parent_solution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='issues.Solution'),
        ),
    ]

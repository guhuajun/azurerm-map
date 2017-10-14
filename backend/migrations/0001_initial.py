# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cmdlet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120, unique=True)),
                ('verb', models.CharField(db_index=True, max_length=20, null=True)),
                ('noun', models.CharField(db_index=True, max_length=100, null=True)),
                ('module', models.CharField(db_index=True, max_length=80)),
            ],
            options={
                'ordering': ('noun',),
            },
        ),
        migrations.CreateModel(
            name='CmdletOutputType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120)),
                ('output_type', models.CharField(db_index=True, max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='CmdletParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120)),
                ('parameter', models.CharField(db_index=True, max_length=240)),
                ('parameter_type', models.CharField(db_index=True, max_length=240)),
                ('parameter_set', models.CharField(db_index=True, max_length=120)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]

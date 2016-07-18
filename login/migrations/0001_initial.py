# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(max_length=50, verbose_name='User Name')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='Email')),
                ('gender', models.CharField(blank=True, max_length=20, null=True, verbose_name='Gender', choices=[(b'Male', b'M'), (b'Female', b'F')])),
                ('contact_no', models.CharField(max_length=20, null=True, verbose_name='Phone', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

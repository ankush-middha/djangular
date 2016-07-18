# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20160707_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff Status'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(max_length=500, null=True, upload_to=login.models.get_profile_image_path, blank=True),
        ),
    ]

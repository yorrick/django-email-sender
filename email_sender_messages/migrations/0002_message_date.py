# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('email_sender_messages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 5, 15, 56, 52, 516321), auto_now=True),
            preserve_default=True,
        ),
    ]

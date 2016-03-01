# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_alter_email_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersocialauth',
            name='private_portal',
            field=models.ForeignKey(related_name='user_social_auth', blank=True, to='privateportal.PrivatePortal', null=True),
        ),
    ]

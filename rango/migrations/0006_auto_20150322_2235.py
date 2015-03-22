# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20150322_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='first_view',
            new_name='first_visit',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='Title',
        ),
    ]

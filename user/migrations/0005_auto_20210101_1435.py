# Generated by Django 2.2 on 2021-01-01 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210101_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 14, 35, 13, 898995)),
        ),
        migrations.AlterField(
            model_name='user',
            name='modfied_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 1, 14, 35, 13, 898995)),
        ),
    ]

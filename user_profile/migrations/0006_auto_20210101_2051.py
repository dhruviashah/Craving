# Generated by Django 2.2 on 2021-01-01 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20210101_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 20, 51, 36, 850623)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='modfied_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 1, 20, 51, 36, 850623)),
        ),
    ]

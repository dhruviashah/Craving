# Generated by Django 2.2 on 2021-01-03 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210101_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 3, 19, 19, 17, 855172)),
        ),
        migrations.AlterField(
            model_name='user',
            name='modfied_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 3, 19, 19, 17, 855172)),
        ),
    ]

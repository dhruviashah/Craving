# Generated by Django 2.2 on 2021-03-14 19:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_auto_20210308_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 0, 55, 27, 285711)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='modfied_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 15, 0, 55, 27, 285711)),
        ),
    ]

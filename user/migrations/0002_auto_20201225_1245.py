# Generated by Django 2.2 on 2020-12-25 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 25, 12, 45, 20, 25152)),
        ),
        migrations.AlterField(
            model_name='user',
            name='modfied_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 25, 12, 45, 20, 25152)),
        ),
    ]

# Generated by Django 2.2 on 2021-03-10 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20210304_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 18, 45, 41, 585943)),
        ),
        migrations.AlterField(
            model_name='user',
            name='modfied_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 18, 45, 41, 585943)),
        ),
    ]

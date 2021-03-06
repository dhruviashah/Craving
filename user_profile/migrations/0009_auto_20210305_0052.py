# Generated by Django 2.2 on 2021-03-04 19:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_auto_20210208_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 5, 0, 52, 33, 761698)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='modfied_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 5, 0, 52, 33, 761698)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='user_role.UserRole'),
        ),
    ]

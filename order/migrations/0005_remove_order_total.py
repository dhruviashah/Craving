# Generated by Django 2.2 on 2021-03-18 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]

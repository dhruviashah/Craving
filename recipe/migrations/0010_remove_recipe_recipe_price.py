# Generated by Django 2.2 on 2021-01-03 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_auto_20210101_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_price',
        ),
    ]

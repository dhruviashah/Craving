# Generated by Django 2.2 on 2021-01-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_recipe_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
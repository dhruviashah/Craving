# Generated by Django 2.2 on 2021-01-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_ingredient', '0003_recipeingredient_unit_converter'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2 on 2021-01-12 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit_of_measure', '0001_initial'),
        ('ingredient', '0004_remove_ingredient_unit_of_measure'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit_converter',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='unit_of_measure.UnitOfMeasure'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.7 on 2019-05-30 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20190530_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('entrees', 'entrees'), ('sweets', 'sweets'), ('beverages', 'beverages')], max_length=60),
        ),
    ]

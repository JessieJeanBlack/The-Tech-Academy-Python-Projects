# Generated by Django 2.0.7 on 2019-05-31 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20190530_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('sweets', 'sweets'), ('entrees', 'entrees'), ('beverages', 'beverages'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]

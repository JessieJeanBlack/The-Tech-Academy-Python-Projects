# Generated by Django 2.0.7 on 2019-05-30 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20190530_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('beverages', 'beverages'), ('entrees', 'entrees'), ('appetizers', 'appetizers'), ('sweets', 'sweets')], max_length=60),
        ),
    ]

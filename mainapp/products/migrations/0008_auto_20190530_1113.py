# Generated by Django 2.0.7 on 2019-05-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20190530_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('beverages', 'beverages'), ('appetizers', 'appetizers'), ('entres', 'entres'), ('sweets', 'sweets')], max_length=60),
        ),
    ]

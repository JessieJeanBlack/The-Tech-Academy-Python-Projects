# Generated by Django 2.0.7 on 2019-05-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20190531_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('sweets', 'sweets'), ('beverages', 'beverages'), ('appetizers', 'appetizers'), ('entrees', 'entrees')], max_length=60),
        ),
    ]
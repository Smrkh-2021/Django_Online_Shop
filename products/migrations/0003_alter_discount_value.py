# Generated by Django 4.0.2 on 2022-02-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_discount_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='value',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-23 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='products.discount'),
        ),
    ]

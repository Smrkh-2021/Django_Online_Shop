# Generated by Django 4.0.2 on 2022-03-25 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_address_alley_alter_address_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lname',
        ),
    ]

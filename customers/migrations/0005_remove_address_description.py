# Generated by Django 4.0.2 on 2022-04-02 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_remove_customer_email_remove_customer_fname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='description',
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-15 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('modify_datetime', models.DateTimeField(auto_now=True)),
                ('delete_datetime', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('modify_datetime', models.DateTimeField(auto_now=True)),
                ('delete_datetime', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('province', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=50)),
                ('alley', models.CharField(max_length=50)),
                ('number', models.PositiveIntegerField()),
                ('description', models.TextField(help_text='Enter your extra description of your address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]

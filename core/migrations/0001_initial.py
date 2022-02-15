# Generated by Django 4.0.2 on 2022-02-15 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('modify_datetime', models.DateTimeField(auto_now=True)),
                ('delete_datetime', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('expire_time', models.DateField(null=True)),
                ('max_price', models.PositiveIntegerField()),
                ('value', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('price', 'Price'), ('percent', 'Percent')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

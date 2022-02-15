# Generated by Django 4.0.2 on 2022-02-14 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OffCode',
            fields=[
                ('basediscount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basediscount')),
                ('code', models.PositiveIntegerField(blank=True, help_text='Off Code', null=True, verbose_name='off code')),
            ],
            options={
                'verbose_name': 'Offcode',
                'verbose_name_plural': 'Offcodes',
            },
            bases=('core.basediscount',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('modify_datetime', models.DateTimeField(auto_now=True)),
                ('delete_datetime', models.DateTimeField(default=None)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('final_price', models.PositiveIntegerField(default=0, help_text='Final Price', verbose_name='Final Price')),
                ('total_price', models.PositiveIntegerField(default=0, help_text='Total Price', verbose_name='Total Price')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('offcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.offcode')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('modify_datetime', models.DateTimeField(auto_now=True)),
                ('delete_datetime', models.DateTimeField(default=None)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Order Status')),
            ],
            options={
                'verbose_name': 'Off code',
                'verbose_name_plural': 'Off codes',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('modify_datetime', models.DateTimeField(auto_now=True)),
                ('delete_datetime', models.DateTimeField(default=None)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('count', models.PositiveIntegerField(default=0, help_text='OrderItem Count', verbose_name='Count')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.status'),
        ),
    ]

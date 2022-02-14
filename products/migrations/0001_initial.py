# Generated by Django 4.0.2 on 2022-02-14 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('modify_datetime', models.DateTimeField(auto_now=True)),
                ('delete_datetime', models.DateTimeField(default=None)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('modify_datetime', models.DateTimeField(auto_now=True)),
                ('delete_datetime', models.DateTimeField(default=None)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('modify_datetime', models.DateTimeField(auto_now=True)),
                ('delete_datetime', models.DateTimeField(default=None)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(help_text='Enter Text Demand')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('basediscount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basediscount')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
            bases=('core.basediscount',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('modify_datetime', models.DateTimeField(auto_now=True)),
                ('delete_datetime', models.DateTimeField(default=None)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('image', models.FileField(upload_to='')),
                ('count', models.PositiveIntegerField(help_text='Number of Products item in Repository')),
                ('color', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('dimension', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('weight', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('properties', models.TextField(help_text='Enter Details of your products')),
                ('brand', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.discount')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.discount'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]

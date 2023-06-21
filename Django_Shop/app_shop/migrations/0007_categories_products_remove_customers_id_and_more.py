# Generated by Django 4.2.2 on 2023-06-21 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0006_rename_firs_name_customers_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.TextField(max_length=50)),
                ('category_description', models.TextField(max_length=50)),
                ('category_image', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('Product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Product_name', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.TextField(max_length=200)),
                ('category_id', models.TextField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='customers',
            name='id',
        ),
        migrations.AddField(
            model_name='customers',
            name='Customer_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('Order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Order_date', models.TextField(max_length=50)),
                ('total_amount', models.TextField(max_length=50)),
                ('payment_type', models.DecimalField(decimal_places=2, max_digits=10)),
                ('state', models.TextField(max_length=200)),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shop.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_name', models.TextField(max_length=50)),
                ('quantity', models.TextField(max_length=50)),
                ('item_notes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_discount', models.TextField(max_length=50)),
                ('item_total', models.TextField(max_length=50)),
                ('item_status', models.TextField(max_length=50)),
                ('Order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shop.orders')),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shop.products')),
            ],
        ),
    ]
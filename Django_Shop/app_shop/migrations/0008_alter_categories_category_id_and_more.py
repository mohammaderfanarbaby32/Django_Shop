# Generated by Django 4.2.2 on 2023-06-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0007_categories_products_remove_customers_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='Customer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='Product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
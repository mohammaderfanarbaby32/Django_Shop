# Generated by Django 4.2.2 on 2023-06-20 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0003_customers_delete_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='Customers_ID',
        ),
    ]

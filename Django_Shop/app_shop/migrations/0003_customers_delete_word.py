# Generated by Django 4.2.2 on 2023-06-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0002_rename_meaning_word_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customers_ID', models.CharField(max_length=100)),
                ('firs_name', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=50)),
                ('emali', models.TextField(max_length=100)),
                ('phone_number', models.TextField(max_length=20)),
                ('Address', models.TextField(max_length=200)),
                ('City', models.TextField(max_length=50)),
                ('state', models.TextField(max_length=50)),
                ('postal_Code', models.TextField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]

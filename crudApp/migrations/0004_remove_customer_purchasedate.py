# Generated by Django 4.0.1 on 2022-02-19 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0003_alter_customer_purchasedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='purchaseDate',
        ),
    ]

# Generated by Django 4.0.1 on 2022-02-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='purchaseDate',
            field=models.DateField(default='date'),
        ),
    ]

# Generated by Django 3.2.12 on 2022-03-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='order_id',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payment_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

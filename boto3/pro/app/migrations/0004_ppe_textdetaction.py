# Generated by Django 3.2.12 on 2022-03-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220217_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='ppe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture1', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='textdetaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture1', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

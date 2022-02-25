# Generated by Django 3.2.12 on 2022-02-25 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('0', 'Male'), ('1', 'Female'), ('2', 'Transgender')], max_length=15)),
                ('number', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('seat_no', models.CharField(blank=True, max_length=4)),
                ('p_status', models.BooleanField(default=False)),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.travel_schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=200)),
                ('order_id', models.CharField(max_length=200)),
                ('signature', models.CharField(max_length=200)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.booking')),
            ],
        ),
    ]

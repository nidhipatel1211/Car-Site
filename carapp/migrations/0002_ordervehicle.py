# Generated by Django 2.2.12 on 2023-06-03 00:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_order_vehicle', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('0', 'Cancelled Order'), ('1', 'Placed Order'), ('2', 'Shipped Order'), ('3', 'Delivered Order')], default='A', max_length=1)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_vehicle_buyer', to='carapp.Buyer')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_vehicle', to='carapp.Vehicle')),
            ],
        ),
    ]
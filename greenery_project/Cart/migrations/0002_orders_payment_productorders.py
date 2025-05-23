# Generated by Django 5.0.4 on 2024-05-17 04:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
        ('Customer', '0001_initial'),
        ('Shop', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default='my_address', max_length=300)),
                ('delivery_status', models.BooleanField(default=False)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('quantity', models.IntegerField(default=0)),
                ('payment_type', models.IntegerField(choices=[(1, 'Cash On Delivery'), (2, 'Online Payment')])),
                ('payment_status', models.BooleanField(default=False)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cart.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.customerdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=265)),
                ('name', models.CharField(max_length=40)),
                ('expiry_month', models.CharField(max_length=2)),
                ('expiry_year', models.CharField(max_length=2)),
                ('cvv', models.CharField(max_length=3)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cart.orders')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.customerdetails')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('delivery_status', models.BooleanField(default=False)),
                ('product_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cart.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Shop.greeneryproducts')),
            ],
        ),
    ]

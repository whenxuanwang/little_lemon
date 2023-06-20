# Generated by Django 4.2.2 on 2023-06-19 22:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_alter_booking_id_alter_booking_no_of_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Inventory',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MaxValueValidator(20.0), django.core.validators.MinValueValidator(2.0)]),
        ),
    ]

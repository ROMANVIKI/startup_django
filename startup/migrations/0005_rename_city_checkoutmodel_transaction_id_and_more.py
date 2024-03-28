# Generated by Django 5.0.2 on 2024-03-28 05:13

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0004_alter_checkoutmodel_company_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutmodel',
            old_name='city',
            new_name='transaction_id',
        ),
        migrations.RenameField(
            model_name='checkoutmodel',
            old_name='country',
            new_name='upi_id',
        ),
        migrations.RemoveField(
            model_name='checkoutmodel',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='checkoutmodel',
            name='state',
        ),
        migrations.RemoveField(
            model_name='checkoutmodel',
            name='street_address',
        ),
        migrations.RemoveField(
            model_name='checkoutmodel',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='checkoutmodel',
            name='package_price',
            field=models.IntegerField(choices=[(1000, '1000'), (5000, '5000'), (10000, '10000')], default=True),
        ),
        migrations.AddField(
            model_name='checkoutmodel',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region='IN'),
        ),
        migrations.AddField(
            model_name='checkoutmodel',
            name='qr_code',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
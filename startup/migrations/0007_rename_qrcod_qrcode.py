# Generated by Django 5.0.2 on 2024-03-28 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0006_qrcod_remove_checkoutmodel_qr_code'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QrCod',
            new_name='QrCode',
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0008_alter_qrcode_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='qr_code',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-28 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0005_rename_city_checkoutmodel_transaction_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QrCod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code', models.ImageField(default=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='checkoutmodel',
            name='qr_code',
        ),
    ]
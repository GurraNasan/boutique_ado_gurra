# Generated by Django 3.2 on 2023-01-24 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_rename_phoone_number_order_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='Order',
            new_name='order',
        ),
    ]

# Generated by Django 3.2 on 2021-05-09 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShipTransactionMS', '0011_remove_inventory_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='originalInventory',
        ),
    ]

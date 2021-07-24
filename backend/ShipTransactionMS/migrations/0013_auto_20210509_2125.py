# Generated by Django 3.2 on 2021-05-09 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShipTransactionMS', '0012_remove_inventory_originalinventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='applicationsNumber',
            new_name='applicationsQuantity',
        ),
        migrations.AddField(
            model_name='application',
            name='note',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='orderId',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='suppliers',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='agreePersonnel',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
# Generated by Django 3.2 on 2021-05-08 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShipTransactionMS', '0006_department_personnel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnel',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Personnel',
        ),
    ]

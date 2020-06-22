# Generated by Django 3.0.6 on 2020-05-26 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20200522_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderregister',
            name='status',
            field=models.CharField(choices=[('ORDERED', 'ORDERED'), ('APPROVED', 'APPROVED'), ('CONFIRMED', 'CONFIRMED'), ('PACKING', 'PACKING'), ('SHIPPED', 'SHIPPED'), ('RETURNED', 'RETURNED'), ('RECEIVED', 'RECEIVED'), ('CLOSED', 'CLOSED'), ('PURCHASED', 'PURCHASED')], default='ORDERED', max_length=20),
        ),
    ]

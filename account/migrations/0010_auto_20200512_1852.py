# Generated by Django 2.2.12 on 2020-05-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200512_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='amount_paid',
        ),
        migrations.RemoveField(
            model_name='company',
            name='amount_to_be_paid',
        ),
        migrations.AddField(
            model_name='company',
            name='payment_due',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='company',
            name='payment_received',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='company',
            name='payment_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

# Generated by Django 2.2.12 on 2020-05-10 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200510_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Company'),
            preserve_default=False,
        ),
    ]

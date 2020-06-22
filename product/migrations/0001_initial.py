# Generated by Django 3.0.5 on 2020-04-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productMaterialItemCode', models.CharField(max_length=100)),
                ('productBrandNewSellingRate', models.FloatField()),
                ('productLossRate', models.FloatField()),
                ('productRepairRate', models.FloatField()),
                ('productDailyRentalRate', models.FloatField()),
                ('productWeekyRentalRate', models.FloatField()),
                ('productMonthlyRentalRate', models.FloatField()),
                ('productDailyHireCharge', models.FloatField()),
                ('productWeekyHireCharge', models.FloatField()),
                ('productMonthlyHireCharge', models.FloatField()),
                ('productRecordedBy', models.CharField(max_length=100)),
                ('supplierName', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=200)),
            ],
        ),
    ]
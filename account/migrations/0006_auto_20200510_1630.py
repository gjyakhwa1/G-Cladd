# Generated by Django 2.2.12 on 2020-05-10 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_remove_profile_recorded_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Company'),
        ),
        migrations.AddField(
            model_name='profile',
            name='recorded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

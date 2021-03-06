# Generated by Django 3.0.6 on 2020-05-06 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torsion_shop', '0005_auto_20200505_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='customer',
            name='account_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_account', to=settings.AUTH_USER_MODEL),
        ),
    ]

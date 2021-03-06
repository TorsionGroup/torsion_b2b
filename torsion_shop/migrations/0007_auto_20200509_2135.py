# Generated by Django 3.0.6 on 2020-05-09 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torsion_shop', '0006_auto_20200506_1851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'RatingStar', 'verbose_name_plural': 'RatingStars'},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='account_id',
        ),
        migrations.AddField(
            model_name='account',
            name='customer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='torsion_shop.Customer'),
        ),
    ]

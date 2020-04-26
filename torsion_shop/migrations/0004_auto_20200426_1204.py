# Generated by Django 3.0.4 on 2020-04-26 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torsion_shop', '0003_auto_20200426_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand_id',
        ),
        migrations.AddField(
            model_name='product',
            name='brand_id',
            field=models.ManyToManyField(related_name='product_brand', to='torsion_shop.Brand'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torsion_shop.Product'),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-05 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torsion_shop', '0004_auto_20200505_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='torsion_shop.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='torsion_shop.CatalogCategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='offer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='torsion_shop.Offer'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_category',
        ),
        migrations.AddField(
            model_name='product',
            name='price_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='torsion_shop.PriceCategory'),
        ),
    ]

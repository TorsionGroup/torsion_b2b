# Generated by Django 3.0.6 on 2020-05-05 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torsion_shop', '0006_auto_20200505_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogcategory',
            name='parent_id',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='torsion_shop.CatalogCategory'),
        ),
    ]

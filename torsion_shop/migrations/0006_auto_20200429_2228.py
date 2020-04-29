# Generated by Django 3.0.5 on 2020-04-29 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torsion_shop', '0005_auto_20200429_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='url',
        ),
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='enabled',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='brand',
            name='gallery_attribute',
            field=models.CharField(default='article', max_length=250),
        ),
        migrations.AlterField(
            model_name='brand',
            name='gallery_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='is_recommended',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='brand',
            name='kind',
            field=models.CharField(default='secondary', max_length=250),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=300, null=True, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='sort_index',
            field=models.IntegerField(default=999),
        ),
        migrations.AlterField(
            model_name='brand',
            name='source_id',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='source_type',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='wait_list',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='mult',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name_eng',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='rate',
            field=models.DecimalField(decimal_places=5, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='source_id',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='title',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='pricecategory',
            name='inner_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='pricecategory',
            name='source_id',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ABC',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='advanced_description',
            field=models.TextField(null=True, verbose_name='Advanced description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand_id',
            field=models.ManyToManyField(null=True, related_name='product_brand', to='torsion_shop.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.today, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='income_date',
            field=models.DateTimeField(default=datetime.datetime.today, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_exists',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='offer_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pack_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_category',
            field=models.ManyToManyField(null=True, related_name='product_pricecategory', to='torsion_shop.PriceCategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='search_key',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sort_price',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='source_id',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='source_type',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=15, null=True),
        ),
    ]

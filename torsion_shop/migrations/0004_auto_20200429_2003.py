# Generated by Django 3.0.5 on 2020-04-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torsion_shop', '0003_auto_20200428_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='alias',
            field=models.SlugField(max_length=300),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-31 12:36

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0003_rename_blog_slug_product_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='Product_Name', unique=True),
        ),
    ]

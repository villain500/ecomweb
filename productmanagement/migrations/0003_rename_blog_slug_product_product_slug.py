# Generated by Django 4.1.2 on 2022-10-31 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0002_product_blog_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Blog_slug',
            new_name='Product_slug',
        ),
    ]

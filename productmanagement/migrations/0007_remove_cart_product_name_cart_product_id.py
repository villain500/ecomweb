# Generated by Django 4.1.2 on 2022-11-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0006_rename_add_to_cart_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Product_Name',
        ),
        migrations.AddField(
            model_name='cart',
            name='Product_ID',
            field=models.IntegerField(default=None),
        ),
    ]

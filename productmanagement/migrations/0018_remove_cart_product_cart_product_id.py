# Generated by Django 4.1.2 on 2022-12-09 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0017_alter_cart_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Product',
        ),
        migrations.AddField(
            model_name='cart',
            name='Product_Id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='productmanagement.product'),
        ),
    ]

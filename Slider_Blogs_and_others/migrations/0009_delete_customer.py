# Generated by Django 4.1.2 on 2022-12-09 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0016_remove_placed_order_address_placed_order_city_and_more'),
        ('Slider_Blogs_and_others', '0008_alter_customer_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
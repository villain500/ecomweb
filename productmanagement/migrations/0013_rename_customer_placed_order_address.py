# Generated by Django 4.1.2 on 2022-12-08 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0012_placed_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placed_order',
            old_name='Customer',
            new_name='Address',
        ),
    ]

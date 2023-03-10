# Generated by Django 4.1.2 on 2022-10-28 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(default=None, max_length=30)),
                ('Short_Description', models.CharField(default=None, max_length=50)),
                ('Product_Description', models.CharField(default=None, max_length=500)),
                ('Price', models.IntegerField(default=0)),
                ('Product_Image', models.ImageField(upload_to='Products/')),
                ('Category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='productmanagement.categories')),
            ],
        ),
    ]

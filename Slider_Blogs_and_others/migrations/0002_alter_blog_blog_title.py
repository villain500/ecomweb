# Generated by Django 4.1.2 on 2022-10-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slider_Blogs_and_others', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Blog_Title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]

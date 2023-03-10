# Generated by Django 4.1.2 on 2022-12-08 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Slider_Blogs_and_others', '0008_alter_customer_phone_number'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productmanagement', '0011_alter_cart_quantity_alter_cart_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='placed_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField(default=1)),
                ('Ordered_Date', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=50)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Slider_Blogs_and_others.customer')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productmanagement.product')),
                ('Username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

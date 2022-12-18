# from email.policy import default
from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User
# from Slider_Blogs_and_others.models import Customer

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Product(models.Model):
    Product_Name=models.CharField(max_length=30, default=None)
    Category=models.ForeignKey(Categories, on_delete=models.CASCADE,default=None)
    Short_Description=models.CharField(max_length=50, default=None)
    Product_Description=models.CharField(max_length=500, default=None)
    Price=models.IntegerField(default=0)
    Product_Image=models.ImageField(upload_to="Products/")
    Product_slug=AutoSlugField(populate_from='Product_Name',unique=True,null=True,default=None)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    Username=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE, default=None)
    Quantity=models.IntegerField(default=1)

    
    @property
    def product_total(self):
        return self.Quantity * self.Product.Price


STATUS_CHOICES=(
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Canceled','Canceled')
)
class Placed_Order(models.Model):
    Username=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity=models.PositiveIntegerField(default=1)
    Name=models.CharField(max_length=50, default=None)
    City=models.CharField(max_length=50, default=None)
    Full_Address=models.CharField(max_length=200,default=None)
    Phone_Number=models.CharField(max_length=200, default=None)
    Zipcode=models.IntegerField(default=None)
    Ordered_Date=models.DateTimeField(auto_now_add=True)
    Status=models.CharField(max_length=50,choices= STATUS_CHOICES, default='Pending')

    @property
    def product_total(self):
        return self.Quantity * self.Product.Price

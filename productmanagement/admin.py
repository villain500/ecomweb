from django.contrib import admin
from .models import Product
from .models import Categories
from .models import Cart
from .models import Placed_Order
# Register your models here.

#products model programs
class Products(admin.ModelAdmin):
    list_display=('id','Product_Name','Category','Price')
admin.site.register(Product,Products)

#category model programs
admin.site.register(Categories)

#category model programs
class Carts(admin.ModelAdmin):
    list_display=('Username','Product','Quantity')
admin.site.register(Cart,Carts)

#Placed orders model programs
class Orders(admin.ModelAdmin):
    list_display=('Username','Product','Name','City','Full_Address','Phone_Number','Quantity','Ordered_Date','Status')
admin.site.register(Placed_Order,Orders)
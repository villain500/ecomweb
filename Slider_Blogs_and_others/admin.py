from django.contrib import admin
from .models import Slider
from .models import Blog
from .models import Visitors
# Register your models here.

# this admin register is for home page slider
admin.site.register(Slider)#,SliderAdmin


# this admin register is for Blogs
admin.site.register(Blog)

# this admin register is for Count_User
admin.site.register(Visitors)
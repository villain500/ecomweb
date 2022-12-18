from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# this program is for Home page slider
class Slider(models.Model):
    Slider_Image=models.ImageField(upload_to="slider/",default=None)



# this program is for Blogs
class Blog(models.Model):
    Blog_Title=models.CharField(max_length=100,default=None)
    Blog_Description=HTMLField()
    Blog_Image=models.ImageField(upload_to='Blogs')
    Blog_slug=AutoSlugField(populate_from='Blog_Title',unique=True,null=True,default=None)


# Vistiors counting program start here
class Visitors(models.Model):
    Visitors=models.CharField(max_length=50,default=None)
    
    def __str__(self):
        return self.Visitors

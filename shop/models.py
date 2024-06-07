import datetime
import os
from django.db import models

def get_filenme(req,file):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    files="%s%s"%(now_time,file)
    return os.path.join('uploads/',files)

class Category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_filenme,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=get_filenme,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-Default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

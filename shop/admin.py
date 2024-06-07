from django.contrib import admin
from .models import Category,Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','status')

admin.site.register(Category)
admin.site.register(Product)

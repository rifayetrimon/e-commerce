from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','price','discount_price','category','discription','image')
    search_fields =['title','category']
    fields = ['title','price','discount_price','category','discription','image']

admin.site.register(Product,ProductAdmin)

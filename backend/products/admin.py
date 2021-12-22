from django.contrib import admin
from .models.product_model import Product


class Product_Admin(admin.ModelAdmin):

    list_display = [
        'title',
        'price',

    ]
    search_fields = [

        'title',
    ]
    ordering = ['title']
    list_display_links = [
        'title',
    ]

    list_filter = [
        'title',
        
    ]
    list_per_page = 15


admin.site.register(Product,Product_Admin)


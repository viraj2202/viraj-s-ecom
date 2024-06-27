from django.contrib import admin

from apps.product.models import Category, Product, ProductImage

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)

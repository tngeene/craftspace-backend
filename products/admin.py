from django.contrib import admin

from products.models import Category, Medium, Product

# Register your models here
admin.site.register(Category)
admin.site.register(Medium)
admin.site.register(Product)

from django.contrib import admin
from orders.models import cartItem, Order, CustomOrder
# Register your models here.
admin.site.register(cartItem)
admin.site.register(Order)
admin.site.register(CustomOrder)

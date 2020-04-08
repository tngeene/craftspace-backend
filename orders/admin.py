from django.contrib import admin
from orders.models import Cart, Order, CustomOrder
# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(CustomOrder)

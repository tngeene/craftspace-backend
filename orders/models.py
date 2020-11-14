from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import get_object_or_404

from products.models import Medium, Product

User = get_user_model()

class CartItem(models.Model):
    owner = models.ForeignKey(User,related_name='cart_items',on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,related_name='cart_items',on_delete=models.SET_NULL,null=True)
    quantities = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product} {self.quantities}"


ORDER_STATUS = (
    ('placed', 'placed'),
    ('paid', 'paid'),
)

class Order(models.Model):
    status = models.CharField(max_length=15,choices=ORDER_STATUS,default='placed')
#if anyone tries to delete an entry in this look-up table, it prevents from deleting if it is tied to any records
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,related_name='orders')
    first_name = models.CharField(max_length=45,null=True)
    last_name = models.CharField(max_length=45,null=True)
    email = models.EmailField(null=True)
    order_items = models.ManyToManyField(CartItem, related_name='orders')
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    order_total = models.DecimalField(max_digits=50,decimal_places=2,null=True)
    order_date = models.DateTimeField(auto_now_add=True)

    # def total_price(self):
    #     totals = 0
    #     for item in self.order_items.all():
    #         totals += item.total
    #     self.order_total = totals
    #     self.save()

    def __str__(self):
        if self.user is None:
            return f"{self.status} {self.first_name}  {self.last_name} {self.order_total}"
        else:
             return f"{self.status} {self.user} {self.order_total}"


# evaluates if an order has been completed only if the status is paid
    @property
    def is_completed(self):
        return True if self.status == "paid" else False

class CustomOrder(models.Model):
    picture = models.ImageField(upload_to="custom_orders/images",blank=True,null=True)
    description = models.TextField()
    size = models.TextField()
    medium = models.ForeignKey(Medium,on_delete=models.CASCADE,null=True,related_name='custom_orders')
    due_date = models.DateField()
    artist = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'membership_type':'Artist'},related_name='cust_orders')
    requested_by = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='custom_orders',null=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    is_complete = models.BooleanField(default=False)
    price = models.BigIntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.requested_by:
            return f" {self.requested_by.get_full_name()} {self.due_date} {self.artist} "
        return f"{self.due_date} {self.size}"

from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from django.shortcuts import get_object_or_404

User = get_user_model()

class CartItem(models.Model):
    owner = models.ForeignKey(User,related_name='cart_items_owner',on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,related_name='cart_products',on_delete=models.SET_NULL,null=True)
    quantities = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product} {self.quantities}"


ORDER_STATUS = (
    ('placed', 'Placed'),
    ('paid', 'Paid'),
)

class Order(models.Model):
    status = models.CharField(max_length=15,choices=ORDER_STATUS,default='created')
#if anyone tries to delete an entry in this look-up table, it prevents from deleting if it is tied to any records
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    first_name = models.CharField(max_length=45,null=True)
    last_name = models.CharField(max_length=45,null=True)
    email = models.EmailField(null=True)
    order_items = models.ManyToManyField(CartItem)
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

MEDIUM_CHOICES = (
    ('Canvas', 'Canvas'),
    ('Wood', 'Wood'),
    ('Soapstone', 'Soap Stone'),
)

class CustomOrder(models.Model):
    image = models.ImageField(upload_to="custom_orders/images")
    description = models.TextField()
    size = models.TextField()
    medium = models.CharField(max_length=50,choices=MEDIUM_CHOICES)
    due_date = models.DateField()
    artist = models.ForeignKey(User,on_delete=models.CASCADE,related_name='custom_order_artist')
    requested_by = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='requester',null=True)
    phone_number = models.CharField(max_length=20,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.requested_by} {self.due_date} {self.artist} "
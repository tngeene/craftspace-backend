import os

from cloudinary.models import CloudinaryField
from django.db import models
from django.db.transaction import TransactionManagementError
from users.models import UserAccount

from .validators import validate_quantities_available


class Category(models.Model):
    name = models.CharField(max_length=100)
    cover_photo = models.ImageField(null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Medium(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,blank=True,on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500,default="Empty description")
    picture = models.ImageField(upload_to="art/images",null=True,blank=True)
    spin_image = models.FileField(upload_to="art/3d-images", null=True, blank=True)
    price = models.FloatField(default=0.00)
    quantity = models.IntegerField(default=1)
    available = models.PositiveIntegerField(default=1, validators=[validate_quantities_available,])
    uploaded_by = models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name='products')
    is_approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        if self.quantity > 0:
            return True
        else:
            return False

    @property
    def file_type(self):
        file_name = os.path.basename(self.spin_image.name)
        return os.path.splitext(file_name)[1].lstrip('.')

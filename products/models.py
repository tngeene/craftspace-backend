from django.db import models
from users.models import UserAccount

from cloudinary.models import CloudinaryField

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
    image = CloudinaryField('spin',null=True,blank=True)
    price = models.FloatField(default=0.00)
    quantity = models.IntegerField(default=1)
    uploaded_by = models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name='products')
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        return self.quantity > 0
from django.db import models
from users.models import UserAccount
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500,default="Empty description")
    picture = models.ImageField(upload_to="art/images",null=True,blank=True)
    quantity = models.IntegerField(default=1)
    uploaded_by = models.ForeignKey(UserAccount,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        return self.quantity > 0
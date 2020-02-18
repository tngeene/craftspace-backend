from django.db import models
from users.models import UserAccount
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    date = models.DateField(blank=True)
    banner = models.ImageField(blank=True,upload_to='events/banners')
    uploaded_by = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.date} {self.uploaded_by} '
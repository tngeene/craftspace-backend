from django.core.exceptions import ValidationError
from django.db import models

from users.models import UserAccount

from .validators import validate_date


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    date = models.DateField(blank=True, validators=[validate_date])
    time = models.TimeField(null=True)
    banner = models.ImageField(blank=True,upload_to='events/banners')
    venue = models.CharField(null=True,max_length=255)
    ticket_price = models.FloatField(default=0.00, null=True)
    uploaded_by = models.ForeignKey(UserAccount,related_name='events',on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.date} {self.uploaded_by}'

    # check if the event has passed
    @property
    def has_passed(self):
        if self.date < today:
            return True
        else:
            return False

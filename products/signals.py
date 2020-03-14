from django.db.models.signals import pre_delete
from .models import Product
import cloudinary

@receiver(pre_delete, sender=Product)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)
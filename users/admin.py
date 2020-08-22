from django.contrib import admin
from .models import UserAccount,ArtistProfile,CollectorProfile, Rating
# Register your models here.

admin.site.register(UserAccount)
admin.site.register(ArtistProfile)
admin.site.register(CollectorProfile)
admin.site.register(Rating)

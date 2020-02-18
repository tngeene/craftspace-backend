from django.contrib import admin
from .models import UserAccount,ArtistProfile,CollectorProfile
# Register your models here.

admin.site.register(UserAccount)
admin.site.register(ArtistProfile)
admin.site.register(CollectorProfile)

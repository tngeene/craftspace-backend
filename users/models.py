from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token as AuthToken
from .validators import validate_rating

USER_TYPE_CHOICES = (
    ('Artist', 'Artist'),
    ('Collector', 'Collector')
)

class UserAccountManager(UserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, email, password, **extra_fields)

class UserAccount(AbstractUser):
    first_name = models.CharField('First Name',max_length=255)
    last_name = models.CharField('Last Name',max_length=255)
    email = models.EmailField(max_length=254,unique=True)
    phone_number = models.CharField(unique=True,max_length=15)
    membership_type = models.CharField(max_length=15,choices=USER_TYPE_CHOICES,default='Artist')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone_number','membership_type',]

    objects = UserAccountManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

GENDER_CHOICES = [
    ('male', 'male'),
    ('female', 'female'),
]

class BaseProfile(models.Model):
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    bio = models.TextField(blank=True)
    county = models.CharField(max_length=50,null=True)
    birth_place = models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to="users/profile_photos",null=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class ArtistProfile(BaseProfile):
    user = models.OneToOneField(
        UserAccount,on_delete=models.CASCADE, limit_choices_to={'membership_type': 'Artist'},
        related_name='artist_profile'
    )

    def __str__(self):
        return  self.user.username

class CollectorProfile(BaseProfile):
    user = models.OneToOneField(
        UserAccount,on_delete=models.CASCADE, limit_choices_to={'membership_type': 'Collector'},
        related_name='collector_profile'
    )
    billing_address = models.CharField(max_length= 255,blank=True)

    def __str__(self):
        return self.user.username

class Rating(models.Model):
    rating = models.FloatField(default=1.00, validators=[validate_rating,])
    comment = models.TextField(null=True, blank=True)
    artist_profile = models.ForeignKey(ArtistProfile, related_name='ratings', on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    posted_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='ratings_posted')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.posted_by)

    # # make sure that the rating is below 5
    # def save(self, *args, **kwargs):
    #     if(self.rating > 5.0):
    #         raise ValidationError("rating has to be below 5.0")
    #     super().save(*args, **kwargs)

# class Token(AuthToken):
#     auth_key = models.CharField(_('Key'), max_length=40, db_index=True, unique=True)
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, related_name='auth_tokens',
#         on_delete=models.CASCADE, verbose_name=_('User')
#     )
#     name = models.CharField(_('Name'), max_length=64)

    # class Meta:
    #     unique_together = (('user', 'name'),)

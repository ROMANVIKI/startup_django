from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    mobile_number = PhoneNumberField(blank=True, default=None, null=True)
    referral_code = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.username
    

# name email phone number subject message
    

class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(default=None, null=True, blank=True, region='IN')
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.subject + ' - ' + self.name
    

class AnouncementModel(models.Model):
    anouncement = models.CharField(max_length=200)

    def __str__(self):
        return self.anouncement



# For product section---------------------------->


# Create your models here.
class Category(models.Model):
    class CategoryType(models.TextChoices):
        BASIC = 'BC', _('Basic')
        STANDARD = 'STD', _('Standard')
        PROFESSIONAL = 'PNL', _('Professional')

    category_type = models.CharField(
        max_length=3, 
        choices=CategoryType,
        default=CategoryType.BASIC,
    )    

    class Meta:
        ordering = ['category_type']
        indexes = [
            models.Index(fields=['category_type'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_type
    



class Product(models.Model):
    name = models.CharField(max_length=200, default=None)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    slug = models.SlugField(max_length=200)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    point_1 = models.CharField(max_length=200, default=None, blank=True)
    point_2 = models.CharField(max_length=200, default=None, blank=True)
    point_3 = models.CharField(max_length=200, default=None, blank=True)
    point_4 = models.CharField(max_length=200, default=None, blank=True)
    point_5 = models.CharField(max_length=200, default=None, blank=True)
    point_6 = models.CharField(max_length=200, default=None, blank=True)
    point_7 = models.CharField(max_length=200, default=None, blank=True)
    point_8 = models.CharField(max_length=200, default=None, blank=True)
    point_9 = models.CharField(max_length=200, default=None, blank=True)
    point_10 = models.CharField(max_length=200, default=None, blank=True)

    class Meta:
        ordering = ['category']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['category']),
            models.Index(fields=['-created']),
            
        ]

    def __str__(self):
        return self.name
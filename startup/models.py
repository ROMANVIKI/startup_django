from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    mobile_number = PhoneNumberField(blank=True, default=None, null=True)
    referral_code = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.username
    

# name email phone number subject message
    

class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(default=None, null=True, blank=True)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.subject + ' - ' + self.name
    

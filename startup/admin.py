from django.contrib import admin
from .models import CustomUser, ContactModel, Product, Category, AnouncementModel, Purchase, CheckoutModel

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(ContactModel)
admin.site.register(AnouncementModel)
admin.site.register(Category)
admin.site.register(Purchase)
admin.site.register(CheckoutModel)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
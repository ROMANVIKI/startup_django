from django.contrib import admin
from .models import CustomUser, ContactModel, Product, Category

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(ContactModel)

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
from django.contrib import admin
from .models import Customer, ShippingAdress
# Register your models here.

admin.site.register(Customer)
admin.site.register(ShippingAdress)

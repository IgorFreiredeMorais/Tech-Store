from django.contrib import admin

from .models import Product, Category, Manufacturer, Order, OrderItem, Client
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Client)

# Register your models here.

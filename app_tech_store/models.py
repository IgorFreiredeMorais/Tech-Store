from django.db import models
from django.conf import settings

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price  = models.DecimalField(max_digits = 5,decimal_places = 2, blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    telephone = models.TextField(max_length=255, blank=True, null=True)
    email = models.TextField(max_length=255, blank=True, null=True)

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    products = models.ManyToManyField(Product, blank = True)
    total = models.DecimalField(default = 0.00, max_digits=100, decimal_places = 2)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.id)


from django.db import models

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price  = models.DecimalField(max_digits = 10,decimal_places = 2, blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    telephone = models.TextField(max_length=255, blank=True, null=True)
    email = models.TextField(max_length=255, blank=True, null=True)


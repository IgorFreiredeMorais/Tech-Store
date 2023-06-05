from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.TextField(max_length=255, blank=True, null=True)
    location = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price  = models.DecimalField(max_digits = 10,decimal_places = 2, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name    

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    telephone = models.TextField(max_length=255, blank=True, null=True)
    email = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name  

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')

    def __str__(self):
        return f"{self.client.name} Customer request "
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order from {self.order.client.name}, product : {self.product}, quantity : {self.quantity}"
    
    def clean(self):
        if self.quantity > self.product.quantity:
                raise ValidationError(f"A quantidade de {self.product.name} excede o estoque disponível.")
    
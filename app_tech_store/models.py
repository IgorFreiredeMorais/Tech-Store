from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.TextField(max_length=255)
    location = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    description = models.TextField()
    price  = models.DecimalField(max_digits = 10,decimal_places = 2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name    

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    address = models.TextField(max_length=255)
    telephone = models.TextField(max_length=255)
    email = models.TextField(max_length=255)

    def __str__(self):
        return self.name  

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')

    def __str__(self):
        return f"{self.client.name} Customer request {self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, editable = False)

    def __str__(self):
        return f"Order from {self.order.client.name}, product : {self.product}, quantity : {self.quantity}, price: {self.price}"
    
    def clean(self):
        if self.quantity > self.product.quantity:
                raise ValidationError(f"{self.product.name} quantity exceeds available stock. Quantity in Stock : {self.product.quantity}")
    
    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def price_display(self):
        return self.price
    
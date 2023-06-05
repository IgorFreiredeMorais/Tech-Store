from django import forms
from django.forms import ModelForm
from .models import Product, Client, Category, Manufacturer


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name': 'Name',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }

class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('name', 'location')
        labels = {
            'name': 'Name',
            'location': 'Location'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
        }
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price','category', 'quantity', 'image')
        labels = {
            'name': 'Name',
            'description':'Description',
            'price':'Price',
            'category': 'Category',
            'quantity':'Quantity in Stock',
            'image' : 'image'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'quantity':forms.TextInput(attrs={'class':'form-control'}),
        }

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'telephone','address')
        labels = {
            'name': 'Name',
            'email':'Description',
            'telephone':'telephone',
            'address': 'address',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'telephone':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'})
        }

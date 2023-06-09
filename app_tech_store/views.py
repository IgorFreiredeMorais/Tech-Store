from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Client, Category, Manufacturer
from django.core.paginator import Paginator
from .forms import ProductForm, ClientForm, CategoryForm, ManufacturerForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request): 
    search = request.GET.get('search')
    
    if search:
        
        products = Product.objects.filter(name__icontains=search)
    
    else :
        products_list =  Product.objects.all()
        paginator = Paginator(products_list, 8)
        page = request.GET.get('page')
        products = paginator.get_page(page)

    return render(request, 'home.html', {'products':products})

## views do produto
@login_required
def admin_add_products(request):
    manufacturers = Manufacturer.objects.all()
    categorys = Category.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('admin/product/products')
    else:
        form = ProductForm()
    
    return render(request, 'admin/product/addProduct.html', {'form': form, 'categorys': categorys, 'manufacturers': manufacturers})
    
def product(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'product/product.html', {'product': product})
    
@login_required
def update_product(request, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST or None,request.FILES or None, instance=product )
    if form.is_valid():
        form.save()
        return redirect ('list_products')


    return render(request, 'admin/product/updateProduct.html', {'product':product, 'form':form})
@login_required
def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()

    return redirect('list_products')

@login_required
def admin_list_products(request):
    products =  Product.objects.all()

    return render(request, 'admin/product/products.html',{'products':products})


# views do cliente
@login_required
def admin_add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
    else:
        form = ClientForm()
        return render(request, 'admin/client/addClient.html', {'form': form})
    
@login_required
def update_client(request, id):
    client = Client.objects.get(pk=id)
    form = ClientForm(request.POST or None, instance=client )
    if form.is_valid():
        form.save()
        return redirect ('list_clients')


    return render(request, 'admin/client/updateClient.html', {'client':client, 'form':form})

@login_required
def delete_client(request, id):
    client = Client.objects.get(pk=id)
    client.delete()

    return redirect('list_clients')

@login_required
def admin_list_clients(request):
    clients =  Client.objects.all()

    return render(request, 'admin/client/clients.html',{'clients':clients})


# views de category
@login_required
def admin_add_categorys(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_categorys')
    else:
        form = CategoryForm()
        return render(request, 'admin/category/addCategory.html', {'form': form})
    
@login_required
def update_category(request, id):
    category = Category.objects.get(pk=id)
    form = CategoryForm(request.POST or None, instance=category )
    if form.is_valid():
        form.save()
        return redirect ('list_categorys')


    return render(request, 'admin/category/updateCategory.html', {'category':category, 'form':form})

@login_required
def delete_category(request, id):
    category = Category.objects.get(pk=id)
    category.delete()

    return redirect('list_categorys')

@login_required
def admin_list_categorys(request):
    categorys =  Category.objects.all()

    return render(request, 'admin/category/categorys.html',{'categorys':categorys})


# views do fabricante
@login_required
def admin_add_manufacturers(request):
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_manufacturers')
    else:
        form = ManufacturerForm()
        return render(request, 'admin/manufacturer/addManufacturer.html', {'form': form})
    
@login_required
def update_manufacturer(request, id):
    manufacturer = Manufacturer.objects.get(pk=id)
    form = ManufacturerForm(request.POST or None, instance=manufacturer )
    if form.is_valid():
        form.save()
        return redirect ('list_manufacturers')


    return render(request, 'admin/manufacturer/updateManufacturer.html', {'manufacturer':manufacturer, 'form':form})

@login_required
def delete_manufacturer(request, id):
    manufacturer = Manufacturer.objects.get(pk=id)
    manufacturer.delete()

    return redirect('list_manufacturers')

@login_required
def admin_list_manufacturers(request):
    manufacturers =  Manufacturer.objects.all()

    return render(request, 'admin/manufacturer/manufacturers.html',{'manufacturers':manufacturers})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Client
from django.shortcuts import redirect
from django.core.paginator import Paginator
from .forms import ProductForm, ClientForm
from django.contrib.auth.decorators import login_required

def home(request): 
    search = request.GET.get('search')
    
    if search:
        
        products = Product.objects.filter(name__icontains=search)
    
    else :
        products_list =  Product.objects.all()
        paginator = Paginator(products_list, 4)
        page = request.GET.get('page')
        products = paginator.get_page(page)

    return render(request, 'home.html', {'products':products})

## views do produto
@login_required
def admin_add_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
        return render(request, 'admin/product/addProduct.html', {'form': form})
    
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







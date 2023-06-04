from django.urls import path, include
from app_tech_store import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name="home"),
    path('shop-cart', views.shop_cart, name="shop-cart"),
    # urls do produto
    path('admin/product/add-product', views.admin_add_products, name='add_products'),
    path('admin/product/products', views.admin_list_products, name='list_products'),
    path('admin/product/update_product/<int:id>', views.update_product, name='update-product'),
    path('admin/delete_product/<int:id>', views.delete_product, name='delete-product'),

    #urls do cliente
    path('admin/client/add-client', views.admin_add_client, name='add_clients'),
    path('admin/client/clients', views.admin_list_clients, name='list_clients'),
    path('admin/client/update_client/<int:id>', views.update_client, name='update-client'),
    path('admin/delete_client/<int:id>', views.delete_client, name='delete-client'),
    path('admin/',admin.site.urls),

    #urls de users
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]


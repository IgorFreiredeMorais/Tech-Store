from django.urls import path, include
from app_tech_store import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    # urls de categoria
    path('admin/category/add-category', views.admin_add_categorys, name='add_categorys'),
    path('admin/category/categorys', views.admin_list_categorys, name='list_categorys'),
    path('admin/category/update_category/<int:id>', views.update_category, name='update-category'),
    path('admin/delete_category/<int:id>', views.delete_category, name='delete-category'),
    # urls do fabricante
    path('admin/manufacturer/add-manufacturer', views.admin_add_manufacturers, name='add_manufacturers'),
    path('admin/manufacturer/manufacturers', views.admin_list_manufacturers, name='list_manufacturers'),
    path('admin/manufacturer/update_manufacturer/<int:id>', views.update_manufacturer, name='update-manufacturer'),
    path('admin/delete_manufacturer/<int:id>', views.delete_manufacturer, name='delete-manufacturer'),
    # urls do produto
    path('admin/product/add-product', views.admin_add_products, name='add_products'),
    path('admin/product/products', views.admin_list_products, name='list_products'),
    path('admin/product/update_product/<int:id>', views.update_product, name='update-product'),
    path('admin/delete_product/<int:id>', views.delete_product, name='delete-product'),
    path('product/<int:id>', views.product, name='product_details'),

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
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )


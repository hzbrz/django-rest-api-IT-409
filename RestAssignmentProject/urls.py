"""FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from FinalApp import views

# from FinalApp.views import CustomerListCreate, AddressListCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.endpoints, name='home'),
    re_path(r'^listCustomerREST/$', views.CustomerListCreate.as_view(), name='list_customer_REST'),
    path('getAddressREST/<int:fk>/', views.GetAddresses.as_view(), name='get_addresses_REST'),
    re_path(r'^addAddressREST/$', views.AddAddress.as_view(), name='add_address_REST'),
    path('getOrderREST/<int:fk>/', views.GetOrders.as_view(), name='get_orders_REST'),
    re_path(r'^addOrderREST/$', views.AddOrder.as_view(), name='add_order_REST'),
    path('getProductREST/<int:fk>/', views.GetProducts.as_view(), name='get_products_REST'),
    re_path(r'^addProductREST/$', views.AddProduct.as_view(), name='add_product_REST'),
]

from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('', Products.as_view(), name='products'),
    path('create/', createProduct.as_view(), name='create_product'),
    path('read/<int:id>/', read1Product.as_view(), name='read1_product'),  
    path('update/<int:id>/', updateProduct.as_view(), name='update_product'),
    path('delete/<int:id>/', deleteProduct.as_view(), name='delete_product'),
    path('order/<int:id>', makeOrder.as_view(), name='make_order'),
    path('orders/', getOrders.as_view(), name='get_orders'),
    path('pay/', payOrder.as_view(), name='pay_order'),
    path('deleteOrder/<int:id>', deleteProdQ.as_view(), name='delete_order'),

    path('brands/', Brands.as_view(), name='brands'),
    path('brands/create/', createBrand.as_view(), name='create_brand'),
    path('brands/update/<int:id>/', updateBrand.as_view(), name='update_brand'),
    path('brands/delete/<int:id>/', deleteBrand.as_view(), name='delete_brand'),
    
]
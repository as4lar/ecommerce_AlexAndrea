from django.urls import path
from .views import *

urlpatterns=[
    path('', Products.as_view(), name='products'),
    path('create', createProduct.as_view(), name='create_product'),
    path('read/<int:id>/', read1Product.as_view(), name='read1_product'),  
    path('update/<int:id>/', updateProduct.as_view(), name='update_product'),
    path('delete/<int:id>/', deleteProduct.as_view(), name='delete_product'),
    path('order/<int:id>', makeOrder.as_view(), name='make_order'),
    path('pay/', payOrder.as_view(), name='pay_order'),
]
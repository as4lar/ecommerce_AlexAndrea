#urls que van a vivir en la aplicacion, va a ser la principal y nos traemos la vista
from django.urls import path
from .views import *

urlpatterns=[
    path('', Home.as_view(), name='index')
]
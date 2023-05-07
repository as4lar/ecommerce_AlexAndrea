from .views import *
from django.urls import path

urlpatterns=[
    path('', Users.as_view(), name='user'),
    path('create', createUser.as_view(), name='create_user'),
    path('update/<int:id>/', updateUser.as_view(), name='update_user'),
    path('delete/<int:id>/', deleteUser.as_view(), name='delete_user'),
]
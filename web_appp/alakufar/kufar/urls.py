from django.urls import path
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('profile/<int:pk>/', UserDetail.as_view(), name='profile_detail'),
    path('make_profile/', CreateUser.as_view(), name='profile'),
    path('post/<int:pk>/delete/',
         ProductDelete.as_view(), name='prod_delete'),
    path('post/<int:pk>/edit/',
         ProductUpdate.as_view(), name='prod_edit'),
    path('products/new/', CreateProduct.as_view(), name='prod_new'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='prod_detail'),
    path('category/<slug:slug>/', ProductCategory.as_view(), name='prod_of_category')
]
